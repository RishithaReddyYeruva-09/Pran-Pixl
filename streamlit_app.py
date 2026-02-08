<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>App Workspace</title>
    
    <style>
        /* Reset and Base Styles */
        * {
            box-sizing: border-box;
        }
        
        body, html {
            margin: 0;
            padding: 0;
            height: 100%;
            font-family: sans-serif;
            overflow: hidden; /* Prevents double scrollbars */
        }

        /* The 2-Part Layout Container */
        .container {
            display: flex;
            height: 100vh;
            width: 100vw;
        }

        /* Sidebar: 1 part (1/3) */
        .sidebar {
            flex: 1; 
            background-color: #f4f4f4;
            border-right: 1px solid #ccc;
            padding: 20px;
            overflow-y: auto;
        }

        /* Main Content: 2 parts (2/3) */
        .main-section {
            flex: 2;
            background-color: #ffffff;
            padding: 20px;
            overflow-y: auto;
        }
    </style>
</head>
<body>

    <div class="container">
        <aside class="sidebar">
            <h2>Sidebar (1/3)</h2>
            <p>Controls or navigation go here.</p>
        </aside>

        <main class="main-section">
            <h2>Main Content (2/3)</h2>
            <p>Your primary app data goes here.</p>
        </main>
    </div>

    <script>
        console.log("Senior Dev: 1/3 split layout active.");
    </script>
</body>
</html>
