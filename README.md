# doc2pdf

Docker service for generating Pdf data from Doc/Docx using libreoffice.

Command to start:
`docker-compose up`

Url to send requests with doc-data:
POST http://localhost:6000/docx2pdf

In order to use asynchronously, nginx is used as a balancer. 

Example to get PDF-data using Guzzle Client (php):
`$response = $this->client->request(
                'POST',
                'http://localhost:6000/docx2pdf',
                ['multipart' => [
                    [
                        'name'     => 'upload_file',
                        'contents' => fopen($sourceFile, 'r')
                    ]
                ]]
            );
            $pdfData =  $response->getBody()->getContents();
`

Enjoy!