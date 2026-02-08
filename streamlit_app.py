<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vintage Coffee App</title>
    
    <style>
        /* Vintage Color Palette */
        :root {
            --espresso: #3d2b1f;
            --mocha: #6f4e37;
            --latte: #c0a080;
            --cream: #f5f5dc;
            --paper: #ece0d1;
            --border: #a67c52;
        }

        * {
            box-sizing: border-box;
        }
        
        body, html {
            margin: 0;
            padding: 0;
            height: 100%;
            /* Using a Serif font for that vintage feel */
            font-family: 'Georgia', serif;
            background-color: var(--paper);
            color: var(--espresso);
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
            background-color: var(--espresso);
            color: var(--cream);
            border-right: 4px double var(--border);
            padding: 30px;
            overflow-y: auto;
        }

        /* Main Content: 2 parts (2/3) */
        .main-section {
            flex: 2;
            background-color: var(--paper);
            padding: 40px;
            overflow-y: auto;
            /* Subtle parchment texture effect */
            background-image: radial-gradient(var(--paper) 70%, #e3d5c5 100%);
        }

        h2 {
            border-bottom: 2px solid var(--mocha);
            padding-bottom: 10px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .sidebar h2 {
            border-bottom-color: var(--latte);
            color: var(--latte);
        }

        p {
            line-height: 1.6;
            font-style: italic;
        }
    </style>
</head>
<body>

    <div class="container">
        <aside class="sidebar">
            <h2>The Blend</h2>
            <p>Navigation and filters would sit here, wrapped in the warmth of a dark roast.</p>
        </aside>

        <main class="main-section">
            <h2>Main Gallery</h2>
            <p>Your content area now has a parchment-style finish. It's clean, readable, and distinctly vintage.</p>
        </main>
    </div>

    <script>
        console.log("Senior Dev: Vintage Coffee theme applied.");
    </script>
</body>
</html>
