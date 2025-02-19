/** @odoo-module **/

import { registry } from "@web/core/registry";
import { UncaughtCorsError } from "@web/core/errors/error_service";

// INFO: this is needed to avoid intercepting CORS errors from external JS.
function corsErrorHandler(env, error, originalError) {
    if (error instanceof UncaughtCorsError) {
        const errorsToIgnore = [
            "ResizeObserver loop completed with undelivered notifications.",
            "ResizeObserver loop limit exceeded"
        ];
        if (originalError && errorsToIgnore.includes(originalError)) {
            return true;
        }
    }
}

// INFO: sequence needs to be the smallest value so it has priority over the system CORS error handler.
registry.category("error_handlers").add("corsErrorToIgnoreHandler", corsErrorHandler, { sequence: 1 });
