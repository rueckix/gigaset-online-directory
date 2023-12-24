#!/usr/bin/env python3

import gigaset
import settings



if __name__ == '__main__':
    gigaset.app.debug = settings.DEBUG
    gigaset.app.run(host='0.0.0.0', port=settings.PORT)

