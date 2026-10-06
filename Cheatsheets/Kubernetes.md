# Kubernetes Quick Reference

| Task | Command |
|---|---|
| Context and namespace | `kubectl config current-context` · `kubectl config view --minify` |
| Workloads | `kubectl get pods,deployments -A` |
| Services | `kubectl get services -A` |
| Events | `kubectl get events -A --sort-by=.metadata.creationTimestamp` |
| Pod details | `kubectl describe pod POD -n NAMESPACE` |
| Recent logs | `kubectl logs POD -n NAMESPACE --since=1h` |
| RBAC review | `kubectl auth can-i --list -n NAMESPACE` |

Confirm the context and namespace before any command that changes cluster state. Protect output because it may expose names, configuration, or secrets. See [Kubernetes](../Kubernetes/).
