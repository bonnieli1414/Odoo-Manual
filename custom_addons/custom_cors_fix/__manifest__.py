{
    "name": "Custom CORS Fix",
    "version": '17.0.0.1',
    "author": "Bonnie",
    "category": "Tools",
    "description": "Fix CORS issues for ResizeObserver errors",
    "depends": ["web"],
    "data": [],
    "assets": {
        "web.assets_backend": [
            "custom_cors_fix/static/src/js/fix_cors_error.js",
        ],
    },
    "installable": True,
    "application": False,
}
