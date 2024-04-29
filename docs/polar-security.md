## About the connector
An agentless platform that connects within minutes, Polar Security can automatically find unknown and sensitive data across the cloud.
<p>This document provides information about the Polar Security Connector, which facilitates automated interactions, with a Polar Security server using FortiSOAR&trade; playbooks. Add the Polar Security Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Polar Security.</p>

### Version information

Connector Version: 1.0.0


Authored By: Fortinet

Certified: No
## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-polar-security</pre>

## Prerequisites to configuring the connector
- You must have the credentials of Polar Security server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Polar Security server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Polar Security</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the Polar Security server URL to connect and perform the automated operations.
</td>
</tr><tr><td>Username</td><td>Specify the Polar Security username to connect and perform the automated operations.
</td>
</tr><tr><td>Password</td><td>Specify the Polar Security password to connect and perform the automated operations.
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Linked Vendors</td><td>Get a list of all 3rd party vendors connected to cloud workloads.</td><td>get_linked_vendors <br/>Investigation</td></tr>
<tr><td>Get Data Stores</td><td>Get a list of data stores from Polar Security.</td><td>get_data_stores <br/>Investigation</td></tr>
<tr><td>Get Data Stores Summary</td><td>Retrieve the data store summary from Polar Security.</td><td>get_data_stores_summary <br/>Investigation</td></tr>
<tr><td>Get Vendors Data Stores</td><td>Get a list of all vendors data stores.</td><td>get_vendors_data_stores <br/>Investigation</td></tr>
<tr><td>Get Data Store</td><td>Get a data store by specific store ID from Polar Security.</td><td>get_data_store <br/>Investigation</td></tr>
<tr><td>Get Vendor Accessible Data Store</td><td>Get all data stores accessible by 3rd party vendors from Polar Security.</td><td>get_vendor_accessible_data_store <br/>Investigation</td></tr>
<tr><td>Apply Label</td><td>Apply a label to specific data store in Polar Security.</td><td>apply_label <br/>Investigation</td></tr>
</tbody></table>

### operation: Get Linked Vendors
#### Input parameters
None.
#### Output

 The output contains a non-dictionary value.
### operation: Get Data Stores
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Limit</td><td>(Optional) Specify the maximum results to return from Polar Security. The default value is 50.
</td></tr><tr><td>Page Size</td><td>(Optional) Specify the maximum results to return per page from Polar Security. The default value is 50.
</td></tr><tr><td>Next Token</td><td>(Optional) Specify the hash value for the next page from Polar Security.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Data Stores Summary
#### Input parameters
None.
#### Output

 The output contains a non-dictionary value.
### operation: Get Vendors Data Stores
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Vendor ID</td><td>Specify the vendor ID retrieved from action Get Linked Vendors.
</td></tr><tr><td>Limit</td><td>(Optional) Specify the maximum results to return from Polar Security. The default value is 50.
</td></tr><tr><td>Page Size</td><td>(Optional) Specify the maximum results to return per page from Polar Security. The default value is 50.
</td></tr><tr><td>Next Token</td><td>(Optional) Specify the hash value for the next page from Polar Security.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Data Store
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Store ID</td><td>Specify the store ID to fetch from Polar Security.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Vendor Accessible Data Store
#### Input parameters
None.
#### Output

 The output contains a non-dictionary value.
### operation: Apply Label
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Label</td><td>Specify the 256 character max string.
</td></tr><tr><td>Store ID</td><td>Specify the store ID to which the label to apply in Polar Security.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
## Included playbooks
The `Sample - polar-security - 1.0.0` playbook collection comes bundled with the Polar Security connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Polar Security connector.

- Apply Label
- Get Data Store
- Get Data Stores
- Get Data Stores Summary
- Get Linked Vendors
- Get Vendor Accessible Data Store
- Get Vendors Data Stores

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
