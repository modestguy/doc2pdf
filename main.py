import tempfile

from aiohttp import web
import os
import subprocess


async def docx2pdf_handle(request):
    with tempfile.NamedTemporaryFile() as output:
        reader = await request.multipart()
        docx = await reader.next()

        while True:
            chunk = await docx.read_chunk()
            if not chunk:
                break
            output.write(chunk)

        p = subprocess.Popen([
            'libreoffice',
            '--headless',
            '--convert-to',
            '--convert-to',
            'pdf',
            '--outdir',
            os.path.abspath(os.path.dirname(output.name)),
            os.path.abspath(output.name)
        ])
        p.wait()

        path = "{}.pdf".format(output.name)
        response = web.FileResponse(path=path, status=200)
        response.content_type = 'application/pdf'

        await response.prepare(request)

        try:
            with open(path, 'rb') as f:
                while True:
                    chunk = f.read(8192)
                    if not chunk:
                        break
                    response.write(chunk)
                    await response.drain()
        except Exception as ex:
            print(ex)
            response = web.Response(status=400)

        os.remove(path)
        return response

if __name__ == '__main__':
    app = web.Application()
    app.router.add_post('/docx2pdf', docx2pdf_handle)

    web.run_app(app, port=int(os.getenv('PORT', "6000")))