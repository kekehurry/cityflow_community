import os
import time 
from hashlib import md5
from .utils import base642file,text2file

admin_passkey = 'admin/cityflow'
admin_id = md5(admin_passkey.encode()).hexdigest()

def save_workflow(data,source_folder,base_url,admin=False):
    if admin:
        data['author'] = 'CityFlow'
        data['author_id'] = admin_id
    author = data.get('author')
    name = data.get('name') 
    workflow_id = md5(f"{author}/{name}-{time.time()}".encode()).hexdigest()
    screenshot = data.get('screenShot') 
    if screenshot and 'base64' in screenshot:
        screenshot_path = os.path.join(source_folder,f"images/{workflow_id}_{time.strftime('%H-%M-%S')}.png")
        data['screenShot'] = base642file(screenshot_path,screenshot)

    new_modules = []
    for module in data['nodes']:
        module = save_module(module,source_folder,base_url,admin)
        new_modules.append(module)
    data['nodes'] = new_modules
    return data
    

def save_module(module,source_folder,base_url,admin):
    module_id = module.get('id')
    config = module.get('config')
    icon = config.get('icon')
    if admin:
        config['author'] = 'CityFlow'
        config['author_id'] = admin_id
    if icon:
        icon_path = os.path.join(source_folder,f"icons/{module_id}.png")
        icon_data = config['icon']
        if 'base64' in icon_data:
            request_path = base642file(icon_path,icon)
            config['icon'] = base_url+f"/source/{request_path}"

    files = config.get('files',[])
    file_urls = []
    for file in files:
        file_data = file.get('data')
        file_path = file.get('path')
        file_id = md5(f"{module_id}/{file_path}".encode()).hexdigest()
        file_path = os.path.join(source_folder,f"files/{file_id}")
        if 'base64' in file_data:
            request_path = base642file(file_path,file_data)
            file['data'] = base_url+f"/source/{request_path}"
        file_urls.append(file)
    config['files'] = file_urls

    html = config.get('html')
    if html:
        html_id = md5(f"{module_id}/{html}".encode()).hexdigest()
        html_path = os.path.join(source_folder,f"html/{html_id}")
        if not html.startswith('/api/dataset/source'):
            request_path = text2file(html_path,html)
            config['html'] = base_url+f"/source/{request_path}"
    # update the module config
    module['config'] = config
    return module