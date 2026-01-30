# Apply the manifests for app1
kubectl apply -f app1.yaml

kubectl port-forward service/simple-web-service 8080:80   # Keep this terminal open
http://localhost:8080

# Apply the manifests for app2
kubectl apply -k Node-refresh-operator/test_apps/kubernetes-sample-apps-master/bookinfo-example/kustomize
kubectl port-forward service/productpage -n bookinfo 9080:9080
http://localhost:9080

