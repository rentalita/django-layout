<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="utf-8">
    <title>@Ovid@ - Hola</title>
    <!--[if lt IE 9]>
        <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->
    <link type="text/css" rel="stylesheet"
          href="/static/bootstrap.css">
    <style type="text/css">
      body {
        padding-top: 60px;
      }
    </style>
    <script type="text/javascript" language="javascript"
            src="/libjs/jquery/jquery.min.js">
    </script>
    {% ifequal MAINTENCE_MODE "PRODUCTION" %}
      {% include "@ovid@-google-analytics.tmpl" %}
    {% endifequal %}
  </head>
  <body>
    <div class="topbar">
      <div class="fill">
        <div class="container">
          <h3>
            <a href="/@ovid@/">
              Bienvenido a @Ovid@
            </a>
          </h3>
        </div>
      </div>
    </div>
    <div class="container">
