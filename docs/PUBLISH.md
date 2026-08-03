# Publishing model

1. Actions runs probes and writes `dist/fsl*`
2. Assets upload to release tag **`dist`** with `--clobber` (overwrite each run)
3. Stable URLs via `/releases/latest/download/<code>`
4. Git commit only lightweight `STATUS.json` (optional)

No large profile blobs in git history.
