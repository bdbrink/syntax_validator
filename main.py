import json
import yaml
import hcl2

from kubernetes import client, config
from prometheus_api_client import PrometheusConnect
from grafanalib.core import GrafanaDashboard
from prometheus_alert_parser import Alert

def check_json_syntax(file_path):
    try:
        with open(file_path, 'r') as file:
            json.load(file)
        print(f"{file_path} has valid JSON syntax.")
    except json.JSONDecodeError as e:
        print(f"Error in {file_path}: Invalid JSON syntax.")
        print(e)

def check_yaml_syntax(file_path):
    try:
        with open(file_path, 'r') as file:
            yaml.safe_load(file)
        print(f"{file_path} has valid YAML syntax.")
    except yaml.YAMLError as e:
        print(f"Error in {file_path}: Invalid YAML syntax.")
        print(e)

def check_kubernetes_yaml(file_path):
    try:
        config.load_kube_config()
        k8s_client = client.ApiClient()
        with open(file_path, 'r') as file:
            client.ExtensionsV1beta1Api(k8s_client).read_namespaced_deployment(
                body=yaml.safe_load(file),
                namespace="default"
            )
        print(f"{file_path} has valid Kubernetes syntax.")
    except Exception as e:
        print(f"Error in {file_path}: Invalid Kubernetes syntax.")
        print(e)

def check_prometheus_query(query):
    try:
        prom = PrometheusConnect()
        result = prom.custom_query(query)
        print(f"The query '{query}' is valid.")
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error in Prometheus query '{query}': {e}")

def validate_grafana_dashboard(dashboard):
    try:
        GrafanaDashboard.from_json(dashboard)
        print("Grafana dashboard is valid.")
    except Exception as e:
        print(f"Error in Grafana dashboard: {e}")

def validate_terraform_file(file_path):
    try:
        with open(file_path, 'r') as file:
            hcl2.load(file)
        print(f"{file_path} has valid Terraform configuration.")
    except Exception as e:
        print(f"Error in {file_path}: Invalid Terraform configuration.")
        print(e)


def validate_prometheus_alert(alert):
    try:
        Alert.parse_raw(alert)
        print("Prometheus alert rule is valid.")
    except Exception as e:
        print(f"Error in Prometheus alert rule: {e}")

def main():
    file_path = input("Enter the file path: ")
    if file_path.endswith('.json'):
        check_json_syntax(file_path)
    elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
        check_yaml_syntax(file_path)
        check_kubernetes_yaml(file_path)
    else:
        print("Unsupported file format. Please provide a JSON or YAML file.")
    
    prometheus_query = input("Enter Prometheus query to check syntax: ")
    check_prometheus_query(prometheus_query)

    grafana_dashboard = input("Enter Grafana dashboard JSON: ")
    validate_grafana_dashboard(grafana_dashboard)
    
    terraform_file = input("Enter Terraform configuration file path: ")
    validate_terraform_file(terraform_file)

if __name__ == "__main__":
    main()
