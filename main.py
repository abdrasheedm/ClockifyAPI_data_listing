import requests


''' Clockify Domain '''

DOMAIN = 'https://api.clockify.me/api/v1'


''' Function for getting API Key from saved file '''

def get_api_key():
    try:
        with open('api_ke.txt', 'r') as file:
            api_key = file.read()
            return api_key
    except:
        raise Exception("There is no file named \'api_key.txt\' in your directory")


''' Function to generate header '''

def get_headers():
    api_key = get_api_key()
    headers = {
        'x-api-key' : api_key
    }
    return headers


''' Function to list all workspaces data '''

def get_all_workspaces():
    
    end_point = '/workspaces/'
    url = DOMAIN + end_point
    headers = get_headers()
    response = requests.get(url=url, headers=headers)
    return response.json()
    

''' Function to list all users in a workspace with filter options '''

def get_all_users_in_workspace(workspace_id, name = None, email = None):

    end_point = f'/workspaces/{workspace_id}/users/'
    url = DOMAIN + end_point
    headers = get_headers()
    params = {
        'name' : name,
        'email' : email
    }
    response = requests.get(url=url, headers=headers, params=params)

    return response.json()


''' Function to list clients in a workspace with filter options'''

def get_clients_in_workspace(workspace_id, client_id = None, client_name = None):
    
    end_point = f'/workspaces/{workspace_id}/clients/'
    if client_id:
        end_point = end_point + client_id
    url = DOMAIN + end_point
    headers = get_headers()
    params = {
        'name' : client_name
    }
    response = requests.get(url=url, headers=headers, params=params)
    return response.json()


''' Function to list projects in a workspace with filter options '''

def get_projects_in_workspace(workspace_id, project_id = None, project_name = None):
    
    end_point = f'/workspaces/{workspace_id}/projects/'
    if project_id:
        end_point = end_point + project_id
    url = DOMAIN + end_point
    headers = get_headers()
    params = {
        'name' : project_name
    }
    response = requests.get(url=url, headers=headers, params=params)
    return response.json()


''' Function to list tasks assigned for specific projects '''

def find_tasks_on_project(workspace_id, project_id, task_id = None, task_name = None):

    end_point = f'/workspaces/{workspace_id}/projects/{project_id}/tasks/'
    if task_id:
        end_point = end_point + task_id
    url = DOMAIN + end_point
    headers = get_headers()
    params = {
        'name' : task_name
    }
    response = requests.get(url=url, headers=headers, params=params)
    return response.json()


''' Function to list all groups in a workspace '''

def get_all_groups(wordspace_id, group_name = None):
    
    end_point = f'/workspaces/{wordspace_id}/user-groups/'
    url = DOMAIN + end_point
    headers = get_headers()
    params = {

        'name' : group_name

    }
    response = requests.get(url = url, headers = headers, params = params)

    return response.json()



if __name__ == '__main__':
    try:

        result = get_all_workspaces()
        # result = get_all_users_in_workspace()
        # result = get_clients_in_workspace('5e79d685ff66a323df52686c',  client_name='Mailshake')
        # result = get_projects_in_workspace('5e79d685ff66a323df52686c', project_name='Field Assist')
        # result = find_tasks_on_project('649d53b1d06d057873874d5b', '649daf38d06d05787389a689', task_name='Complete Signup')
        result = get_all_groups('649d53b1d06d057873874d5b')
        print(result)

        
    except TypeError:
        print("Please provide all mandatory parameters")
    
    except Exception as e:
        print(f"An error has occured : {e}")
   
