#!/usr/bin/env python
import intersight
import intersight.api.workflow_api
import credentials
from intersight.api.workflow_api import WorkflowApi
from intersight.model.workflow_workflow_info import WorkflowWorkflowInfo
from intersight.model.mo_base_mo_relationship import MoBaseMoRelationship
from intersight.model.workflow_initiator_context import WorkflowInitiatorContext
from intersight.model.workflow_workflow_definition_relationship import WorkflowWorkflowDefinitionRelationship
from pprint import pprint

moId = "Workflow run MoId"

mo = WorkflowWorkflowInfo(
    action="Start",
    associated_object=MoBaseMoRelationship(
        class_id="mo.MoRef",
        moid="Organization MoId",
        object_type="organization.Organization"
    ),
    input={
        "EmailAddress": "cjohanns@cisco.com",
        "MessageContents": "Test from a python script... Cheers"},
    name="Send Message to Webex Teams",
    workflow_definition=WorkflowWorkflowDefinitionRelationship(
        class_id="mo.MoRef",
        moid="Workflow Definition MoId",
        object_type="workflow.WorkflowDefinition"
    )
)

def create_workflow_workflow_info(apiClient,mo):
    print("Email address: "+mo.input['EmailAddress'])
    api_instance = intersight.api.workflow_api.WorkflowApi(apiClient)
    workflow = api_instance.create_workflow_workflow_info(mo)

def main():
    apiClient = credentials.config_credentials()
    try:
        create_workflow_workflow_info(apiClient,mo)
    except intersight.OpenApiException as e:
        print(e)

if __name__ == "__main__":
    main()
