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

moId = "62017e58696f6e2d338f918cc"

mo = WorkflowWorkflowInfo(
    action="Start",
    associated_object=MoBaseMoRelationship(
        class_id="mo.MoRef",
        moid="5ddea9626972652d32b67d21",
        object_type="organization.Organization"
    ),
    input={
        "EmailAddress": "cjohanns@cisco.com",
        "MessageContents": "Test from a python script... Cheers"},
    name="Send Message to Webex Teams",
    workflow_definition=WorkflowWorkflowDefinitionRelationship(
        class_id="mo.MoRef",
        moid="61b81012696f6e2d33259fba",
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
