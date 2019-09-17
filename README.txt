This app demonstrates IoT event triggering lambda, and rule based cloudwatch events.

Cloudwatch event is configured to trigger the lambda function at a certain time to make sure that a record is inserted by IoT click 
events, if such event is not found, then a SNS message is sent to the designated phone number.

Use Case:

If a person or a thing, scheduled to click the button, doesn't do so, then an alarm is triggered. 
