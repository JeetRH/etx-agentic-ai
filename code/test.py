prompt_template = """You are an expert OpenShift administrator. Your task is to analyze pod logs, summarize the error, and generate a JSON object to create a GitHub issue for tracking. Follow the format in the examples below.
        
        ---
        EXAMPLE 1:
        Input: The logs for pod 'frontend-v2-abcde' in namespace 'webapp' show: ImagePullBackOff: Back-off pulling image 'my-registry/frontend:latest'.

        Output:
        The pod is in an **ImagePullBackOff** state. This means Kubernetes could not pull the container image 'my-registry/frontend:latest', likely due to an incorrect image tag or authentication issues.
        {{\"name\":\"create_issue\",\"arguments\":{{\"owner\":\"redhat-ai-services\",\"repo\":\"etx-agentic-ai\",\"title\":\"Issue with Etx pipeline\",\"body\":\"### Cluster/namespace location\\nwebapp/frontend-v2-abcde\\n\\n### Summary of the problem\\nThe pod is failing to start due to an ImagePullBackOff error.\\n\\n### Detailed error/code\\nImagePullBackOff: Back-off pulling image 'my-registry/frontend:latest'\\n\\n### Possible solutions\\n1. Verify the image tag 'latest' exists in the 'my-registry/frontend' repository.\\n2. Check for authentication errors with the image registry.\"}}}}

        ---
        EXAMPLE 2:
        Input: The logs for pod 'data-processor-xyz' in namespace 'pipelines' show: CrashLoopBackOff. Last state: OOMKilled.

        Output:
        The pod is in a **CrashLoopBackOff** state because it was **OOMKilled**. The container tried to use more memory than its configured limit.
        {{\"name\":\"create_issue\",\"arguments\":{{\"owner\":\"redhat-ai-services\",\"repo\":\"etx-agentic-ai\",\"title\":\"Issue with Etx pipeline\",\"body\":\"### Cluster/namespace location\\npipelines/data-processor-xyz\\n\\n### Summary of the problem\\nThe pod is in a CrashLoopBackOff state because it was OOMKilled (Out of Memory).\\n\\n### Detailed error/code\\nCrashLoopBackOff, Last state: OOMKilled\\n\\n### Possible solutions\\n1. Increase the memory limit in the pod's deployment configuration.\\n2. Analyze the application for memory leaks.\"}}}}
        ---

        NOW, YOUR TURN:

        Input: Review the OpenShift logs for the pod '{pod_name}' in the '{namespace}' namespace. If the logs indicate an error, search for the solution, create a summary message with the category and explanation of the error, and create a Github issue using {{\"name\":\"create_issue\",\"arguments\":{{\"owner\":\"redhat-ai-services\",\"repo\":\"etx-agentic-ai\",\"title\":\"Issue with Etx pipeline\",\"body\":\"<summary of the error>\"}}}}. DO NOT add any optional parameters.

        ONLY tail the last 10 lines of the pod, no more.
        The JSON object formatted EXACTLY as outlined above.
        """

pod_name = "test"
namespace = "test"

formatted_prompt = prompt_template.format(pod_name=pod_name, namespace=namespace)
print(formatted_prompt)
