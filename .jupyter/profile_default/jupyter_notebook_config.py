c = get_config()
c.NotebookApp.server_extensions = [
    'statnlpbook.draw'
]
c.NotebookApp.maxbuffer = 1000000000
c.NotebookApp.max_body_size = 1000000000

print("Yoooo!")