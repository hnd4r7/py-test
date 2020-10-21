from kubernetes import client, config
from kubernetes.stream import stream
import tarfile
from tempfile import TemporaryFile

# create an instance of the API class
config.load_kube_config()
api_instance = client.CoreV1Api()
# #列出 namespaces
# for ns in api_instance.list_namespace().items:
#     print(ns.metadata.name)
#
# #列出所有的nodes
# def list_node():
#     api_response = api_instance.list_node()
#     data = {}
#     for i in api_response.items:
#         data[i.metadata.name] = {"name": i.metadata.name,
#                                  "status": i.status.conditions[-1].type if i.status.conditions[-1].status == "True" else "NotReady",
#                                  "ip": i.status.addresses[0].address,
#                                  "kubelet_version": i.status.node_info.kubelet_version,
#                                  "os_image": i.status.node_info.os_image,
#                                  }
#     return data

# #列出所有的services
# def list_service():
#     api_response = api_instance.list_service_for_all_namespaces()
#     return api_response

#列出所有的pod
def list_pod():
    api_response = api_instance.list_namespaced_pod("local-test")
    data = {}
    for i in api_response.items:
        data[i.metadata.name] = {"ip": i.status.pod_ip, "namespace": i.metadata.namespace}
    return data

#列出所有job
def list_job_for_all_namespaces():
    api_response = api_instance.list_job_for_all_namespaces()
    return api_response

def list_job(namespace="default"):
    api_response = api_instance.list_namespaced_job(namespace)
    return api_response

# kubectl copy
exec_command = ['tar', 'xvf', '-', '-C', '/']
resp = stream(api_instance.connect_get_namespaced_pod_exec, "lll-testvpc-deployment-75974b764f-4zcpv", 'local-test',
              command=exec_command,
              stderr=True, stdin=True,
              stdout=True, tty=False,
              _preload_content=False)

source_file = '/tmp/abc.txt'

with TemporaryFile() as tar_buffer:
    with tarfile.open(fileobj=tar_buffer, mode='w') as tar:
        tar.add(source_file)

    tar_buffer.seek(0)
    commands = []
    commands.append(tar_buffer.read())

    while resp.is_open():
        resp.update(timeout=1)
        if resp.peek_stdout():
            print("STDOUT: %s" % resp.read_stdout())
        if resp.peek_stderr():
            print("STDERR: %s" % resp.read_stderr())
        if commands:
            c = commands.pop(0)
            # print("Running command... %s\n" % c)

            resp.write_stdin(c)
        else:
            break
    resp.close()
