# Modelo do revisor automático

O cron usa `producao/ia.yaml`, uma configuração exclusiva deste projeto. Edite os quatro campos da etapa `revisao_visual`: tipo, motor, modelo e esforco. As cinco combinações estão comentadas com `#` no próprio arquivo. Texto/visão aceitam assinatura Claude/Codex ou APIs Anthropic/OpenAI/OpenRouter. APIs estão desativadas e exigem autorização específica para este sistema.

```bash
python3 producao/ia_motor.py ver
python3 producao/ia_motor.py validar
python3 producao/ia_motor.py configurar revisao_visual --tipo assinatura --motor claude --modelo claude-opus-5-5 --esforco medium
python3 producao/ia_motor.py configurar revisao_visual --tipo assinatura --motor codex --modelo gpt-6.1-sol --esforco medium
```

Alterar a configuração preserva os comentários. O cron lê o arquivo a cada revisão; não precisa reiniciar o timer. Modelo e esforço são passados explicitamente ao CLI. Chaves herdadas de APIs são removidas na assinatura. Não existe fallback automático pago.

O executor anexa roteiro, medições disponíveis e os bytes da folha de quadros (Codex usa `-i`; APIs recebem imagem). Falta de imagem, JSON inválido ou falha do motor retorna erro e mantém o tratamento de tentativas/parada do produtor. O parecer continua sujeito às mesmas regras: defeito reprova; melhoria vira sugestão. Registro local em `ia-execucoes.jsonl` na edição, sem conteúdo de credenciais. A revisão não publica nem altera a edição.

Imagens geradas continuam na assinatura Codex; este arquivo troca o revisor, não o gerador.

Validação em 15/11/2026: seis contratos locais e teste existente da produção passaram; revisão real pela assinatura Codex devolveu parecer aprovado em folha de edição existente, sem publicar. Evidência local em `~/projetos/output/crons-multiprovedor-2026-11-15/r7ex/resultado.json`.

## Crítico do plano e trava de cota (17/11/2026, v1.7.5)

**Crítico (`critico_plano`).** `r7ex.py plano` não chama mais `claude -p` fixo: usa a etapa `critico_plano` deste `ia.yaml`. A ficha (e `inema-design/regras/chamada.md`) vai anexada ao pedido, então a etapa é texto puro e serve para Claude ou Codex. Principal: Claude `claude-opus-5-5`/`low` (o que o crítico usava por herança, D15 calibrado nele). Reserva: Codex `gpt-6.1-sol`/`medium`. `R7X_CRITICO=codex` (VPS só com Codex) continua valendo: põe o Codex primeiro.

Para inverter (Codex principal, Claude reserva), edite os dois no `producao/ia.yaml`: `motor/modelo/esforco` da etapa e a linha `alternativa` (que precisa ser o outro motor). O comando `configurar` sozinho recusa a troca de motor enquanto a alternativa for do mesmo motor. Depois: `python3 producao/ia_motor.py validar`.

**Trava de cota.** Na primeira recusa ESTRUTURADA de cota do Claude Code (JSON `is_error` + `api_error: usage_limit_reached` ou HTTP 429), o executor grava o horário de volta ("resets 9pm (America/Sao_Paulo)"; ilegível = 1 h; 429 momentâneo = 5 min) em `~/.local/state/enginebridge/state.sqlite`, tabela `pools` do EngineBridge (só `blocked`/`until`; `INEMA_COTA_DB` muda o caminho). Até lá, qualquer etapa com esse motor falha na hora, sem abrir o programa. Codex: sem recusa real registrada, então ainda não trava sozinho.

```bash
python3 producao/ia_motor.py cota ver                    # contas e horário de volta
python3 producao/ia_motor.py cota liberar --motor claude # tira a trava antes do horário (ex.: cota voltou antes)
python3 -m enginebridge block --pool codex:$HOME/.codex   # bloqueio manual (no projeto enginebridge); unblock desfaz
```

**Reserva (`alternativa`).** Só assinatura, só capacidade texto/visão, só quando o principal recusou por cota ou limite momentâneo (429), de forma estruturada, ou já está travado. Erro comum, timeout ou resposta inválida nunca trocam de motor. Agente/MCP/imagem nunca usam reserva. O `ia-execucoes.jsonl` registra o motor usado, `sem_cota` e `reserva`.

**Quem chama.** Revisor sem cota devolve `espera` (não conta como erro, uma linha de log por bloqueio). Crítico sem cota reprova com "NÃO reescreva a ficha" para o agente da ficha não gastar as 3 reescritas. `claude -p` automático roda com `--no-session-persistence`.

Teste real em 17/11/2026, mesma ficha (primeiro-cliente-com-ia), cópia isolada: Claude opus-5-5/low 7·6·7·7·8·6·8 (média 7,0, 25 s); Codex gpt-6.1-sol/medium 7·6·8·7·8·7·9 (7,43, 36 s); os dois no formato de 7 notas. 17 contratos de IA e as 16 conferências da produção passaram.
