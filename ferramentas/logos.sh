#!/usr/bin/env bash
# Baixa o pacote de logos de IA/tecnologia (MIT, @lobehub/icons-static-png) para ~/.cache/r7ex/lobe-icons (D13, 20/10/2026).
set -euo pipefail
D=~/.cache/r7ex/lobe-icons; T=$(mktemp -d); cd "$T"
npm pack @lobehub/icons-static-png@1.97.1 --silent >/dev/null && tar xzf lobehub-icons-static-png-*.tgz
mkdir -p "$D" && rm -rf "$D/dark" && cp -r package/dark package/package.json "$D/" && rm -rf "$T"
echo "logos em $D/dark ($(ls "$D/dark" | wc -l) arquivos)"
