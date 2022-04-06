import intersight.api.workflow_api
import credentials

wf_name = "Send Message to Webex Teams"

def get_workflows(apiClient):
    api_instance = intersight.api.workflow_api.WorkflowApi(apiClient)
    workflows = api_instance.get_workflow_workflow_info_list()
    for i in workflows.results:
        if i.name == wf_name:
            print("Name: " + i.name)
            print("Workflow Info MoId: " + i.moid)
            print("Status: " + i.status)
            print("Workflow Definition MoId: " + i.workflow_definition['moid'])
            get_workflow_inputs(apiClient,i.workflow_definition['moid'])

def get_workflow_inputs(apiClient,moId):
    api_instance = intersight.api.workflow_api.WorkflowApi(apiClient)
    workflows = api_instance.get_workflow_workflow_definition_by_moid(moId)
    for k in workflows.permission_resources:
        print("Organization MoId: " + k.moid)
    for i in workflows.input_definition:
        print("Input name: " + i.name)
        print("Input type: " + i.properties['type'])

def main():
    apiClient = credentials.config_credentials()
    try:
        get_workflows(apiClient)
    except intersight.OpenApiException as e:
        print(e)

if __name__ == "__main__":
    main()
