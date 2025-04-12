from quart import Quart, request, jsonify
import os
import aiofiles

async def list_files(directory):
    return os.listdir(directory)

async def upload_file(directory, file):
    async with aiofiles.open(os.path.join(directory, file.filename), "wb") as f:
        content = await file.read()
        await f.write(content)

def setup_sftp_routes(app: Quart):
    @app.route('/sftp/list', methods=['GET'])
    async def list_sftp_files():
        directory = request.args.get('directory', '/default/sftp/path')
        files = await list_files(directory)
        return jsonify(files)

    @app.route('/sftp/upload', methods=['POST'])
    async def upload_sftp_file():
        directory = request.args.get('directory', '/default/sftp/path')
        file = await request.files['file']
        await upload_file(directory, file)
        return jsonify(success=True, message="文件上传成功")