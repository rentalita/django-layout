<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="utf-8">
    <title>@Ovid@.com - Hola</title>
    <!--[if lt IE 9]>
        <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->
    <link type="text/css" rel="stylesheet"
          href="/static/bootstrap.css">
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
              @Ovid@.com
            </a>
          </h3>
        </div>
      </div>
    </div>
    <br />
    <br />
    <br />
    <div class="container">
