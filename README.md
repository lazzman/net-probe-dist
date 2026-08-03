# net-probe-dist

Lab utility: periodically run **HTTP reachability probes** against public endpoint lists, then publish **encoded profile packages** for offline analysis / local runtime experiments.

> Not a product, not a service listing, not user-facing sharing. CI artifact dump only.

## Dist packages

Published under [`dist/`](./dist) (updated ~every 6 hours):

| Code | Meaning (internal) |
| --- | --- |
| `fsl64` | encoded blob |
| `fslyaml` | YAML pack |
| `fslsb` | JSON runtime pack |
| `fslyamlcomp` | legacy YAML pack |

Example:

```text
https://raw.githubusercontent.com/lazzman/net-probe-dist/main/dist/fsl64
```

Change the last path segment to switch package type.

## Automation

- Workflow: `publish-dist` (schedule every 6 hours + manual dispatch)
- Local: `python3 scripts/ci_public_sub_pipeline.py --workspace . --workers 24`

## Safety

- No WireGuard private key files in `dist/`
- Generated data may go stale quickly; lab use only
