import reflex as rx

# NUEVA sección replicando el diseño de la imagen, abajo de la principal
def asset_management_section():
    return rx.vstack(
        rx.text("Built for you", class_name="text-orange-500 font-semibold text-sm text-center"),
        rx.heading(
            "Powerful asset management,\nwithout the clunky system.",
            class_name="text-3xl font-bold text-center text-gray-800"
        ),
        rx.text(
            "Waste less time answering questions & updating docs",
            class_name="text-center text-gray-500 text-lg mb-10"
        ),

        rx.hstack(
            # Columna IZQUIERDA (correcta)
            rx.vstack(
                feature_item("Quick and Easy Tagging", 
                             "Allows you to tag assets with relevant keywords and descriptions, making them easy to search for and categorize."),
                feature_item("Location Tracking", 
                             "Keep track of where your assets are located by syncing and pinning the last item scanned location on a map."),
                feature_item("CSV Export", 
                             "Useful for sharing data with other tools and making insurance claims."),
                class_name="space-y-10 w-1/3"
            ),

            # Imagen central
            rx.image(
                src="Ima2.png",
                alt="Asset Management Mobile App",
                class_name="w-[360px] rounded-lg shadow-lg"
            ),

            # Columna DERECHA (correcta)
            rx.vstack(
                feature_item("QR Code Scanning", 
                             "Scan QR codes on assets using your phone’s camera, making it quick and easy to check assets in and out."),
                feature_item("Inventory", 
                             "Keep track of your most critical inventory pieces, who owns it and what condition they are in."),
                feature_item("Print your own tags", 
                             "Just order sticker paper for your A4 printer and tag away!"),
                class_name="space-y-10 w-1/3"
            ),

            class_name="justify-between items-start w-full max-w-7xl mx-auto"
        ),

        class_name="px-6 py-16 bg-white"
    )

# Componente para cada feature
def feature_item(title, description):
    return rx.vstack(
        rx.icon(tag="circle", class_name="text-orange-500 text-2xl"),
        rx.heading(title, class_name="text-lg font-semibold text-gray-800 text-center"),
        rx.text(description, class_name="text-sm text-gray-600 text-center max-w-xs"),
        class_name="items-center text-center"
    )

# Tu sección original (debe ir arriba, como pediste)
def qr_tracking_section():
    return rx.vstack(
        # Título principal en naranja
        rx.heading(
            "Asset Tracking Infrastructure for Everyone",
            class_name="text-1xl font-bold text-center mb-2 text-orange-500"
        ),
        
        # Subtítulo
        rx.heading(
            "Everything you need to get your\nassets under control & become\nmore efficent",
            
            class_name="text-3xl font-bold text-center mb-4 text-gray-800"
            
        ),
        
        
        # Texto descriptivo
        rx.text(
            "Print your own Asset Tags, attach them to anything you want to track.",
            class_name="text-center text-gray-600 mb-8"
        ),
        
        # Divider
        rx.divider(class_name="my-6 border-gray-300"),
        
        # Botón Early Access
        rx.center(
            rx.button(
                "Request Early Access →",
                class_name="bg-orange-600 text-white px-6 py-3 rounded-lg font-medium hover:bg-blue-700 transition-colors"
            ),
            class_name="mb-10"
        ),
        
        # Imagen principal
        rx.center(
            rx.image(
                src="img1.png",
                alt="QR Tracking System",
                class_name="max-w-4xl rounded-lg shadow-md mt-10"
            )
        ),
        
        class_name="space-y-8 p-8 max-w-7xl mx-auto"
    )

# Página principal
def index():
    return rx.container(
        rx.vstack(
            # Header con logo y navegación
            rx.hstack(
                rx.image(
                    src="logo.png",
                    alt="Company Logo",
                    class_name="h-12 w-auto"
                ),
                rx.spacer(),
                rx.hstack(
                    rx.link("Features", class_name="text-gray-600 hover:text-gray-900"),
                    rx.link("Pricing", class_name="text-gray-600 hover:text-gray-900"),
                    rx.link("Contact", class_name="text-gray-600 hover:text-gray-900"),
                    class_name="hidden md:flex space-x-8"
                ),
                rx.button("Get Beta Access", class_name="bg-orange-500 text-white px-4 py-2 rounded-lg hover:bg-orange-600"),
                class_name="w-full py-4 px-6 border-b border-gray-200"
            ),

            # 1. Sección principal (original tuya)
            qr_tracking_section(),

            # 2. Nueva sección (imagen replicada)
            asset_management_section(),

            class_name="min-h-screen bg-gray-50"
        )
    )


app = rx.App()
app.add_page(index)
