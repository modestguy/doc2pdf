# doc2pdf

Docker service for generating Pdf data from Doc/Docx using libreoffice.

Command to start:
`docker-compose up`

Url to send requests with doc-data:
POST http://localhost:6000/docx2pdf

Example to get PDF-data using Guzzle Client (php):
`$response = $this->client->request(
                'POST',
                'http://localhost:6000',
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