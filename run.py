#!/usr/bin/env python3

import gigaset
import settings
from waitress import serve

if __name__ == '__main__':
    gigaset.app.debug = settings.DEBUG
    
    
    serve(gigaset.app, host="0.0.0.0", port=settings.PORT)

    # gigaset.app.run(host='0.0.0.0', port=settings.PORT)

