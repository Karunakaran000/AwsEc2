from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AWS World</title>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

body{
    overflow:hidden;
    height:100vh;
    font-family:'Segoe UI',sans-serif;
    display:flex;
    justify-content:center;
    align-items:center;
    background:linear-gradient(
        -45deg,
        #0f172a,
        #1e293b,
        #0f766e,
        #1d4ed8
    );
    background-size:400% 400%;
    animation:gradientMove 15s ease infinite;
}

@keyframes gradientMove{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}

.particles{
    position:absolute;
    width:100%;
    height:100%;
    overflow:hidden;
}

.particles span{
    position:absolute;
    display:block;
    width:6px;
    height:6px;
    background:white;
    border-radius:50%;
    opacity:.3;
    animation:float 20s linear infinite;
}

@keyframes float{
    from{
        transform:translateY(100vh);
    }
    to{
        transform:translateY(-10vh);
    }
}

.card{
    position:relative;
    z-index:10;
    width:900px;
    max-width:90%;
    padding:60px;
    text-align:center;

    background:rgba(255,255,255,0.08);

    backdrop-filter:blur(20px);

    border:1px solid rgba(255,255,255,0.15);

    border-radius:30px;

    box-shadow:
        0 8px 32px rgba(0,0,0,.35);
}

.logo{
    font-size:70px;
    margin-bottom:20px;
    animation:pulse 3s infinite;
}

@keyframes pulse{
    50%{
        transform:scale(1.1);
    }
}

h1{
    color:white;
    font-size:4rem;
    font-weight:700;
    margin-bottom:20px;
}

.highlight{
    color:#38bdf8;
}

p{
    color:#e2e8f0;
    font-size:1.3rem;
    line-height:1.8;
}

.badge{
    margin-top:35px;
    display:inline-block;
    padding:14px 30px;
    border-radius:50px;
    color:white;
    background:linear-gradient(
        90deg,
        #06b6d4,
        #2563eb
    );

    font-weight:bold;

    box-shadow:
      0 0 25px rgba(37,99,235,.5);
}

.fadeup{
    animation:fadeUp 1.5s ease;
}

@keyframes fadeUp{
    from{
        opacity:0;
        transform:translateY(50px);
    }
    to{
        opacity:1;
        transform:translateY(0);
    }
}

</style>

</head>

<body>

<div class="particles">
<span style="left:10%;animation-duration:12s"></span>
<span style="left:20%;animation-duration:15s"></span>
<span style="left:30%;animation-duration:10s"></span>
<span style="left:40%;animation-duration:18s"></span>
<span style="left:50%;animation-duration:13s"></span>
<span style="left:60%;animation-duration:16s"></span>
<span style="left:70%;animation-duration:11s"></span>
<span style="left:80%;animation-duration:20s"></span>
<span style="left:90%;animation-duration:14s"></span>
</div>

<div class="card fadeup">

<div class="logo">🌍</div>

<h1>
Welcome to
<span class="highlight">AWS World</span>
</h1>

<p>
Highly Available Cloud Infrastructure powered by
Auto Scaling Groups, Application Load Balancers,
Private Networking, NAT Gateways and modern DevOps practices.
</p>

<div class="badge">
   Welcome to the world of AWS!
</div>

</div>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3022)

    
    