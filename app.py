from jinja2 import Environment, FileSystemLoader

def render_page(template_name, context):
    # Configurar el entorno de Jinja2 para buscar plantillas en la carpeta 'templates'
    env = Environment(loader=FileSystemLoader('templates'))

    try:
        template = env.get_template(template_name)
        return template.render(context)
    except Exception as e:
        return f"Error al renderizar la plantilla: {e}"

if __name__ == "__main__":
    # Datos de ejemplo para pasar a las plantillas
    datos = {
        "titulo": "Mi Proyecto Jinja2",
        "usuario": "Estudiante",
        "mensaje": "¡Bienvenido a la generación dinámica de páginas!"
    }

    print("--- Renderizando index.html ---")
    print(render_page('index.html', datos))

    print("\n--- Renderizando variantes/pagina2.html ---")
    print(render_page('variantes/pagina2.html', datos))
