"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.renameConnectionCommand = void 0;
const baseCommand_1 = require("../common/baseCommand");
const vscode = require("vscode");
const global_1 = require("../common/global");
const constants_1 = require("../common/constants");
const treeProvider_1 = require("../tree/treeProvider");
'use strict';
class renameConnectionCommand extends baseCommand_1.default {
    run(treeNode) {
        return __awaiter(this, void 0, void 0, function* () {
            let selectedConnection = null;
            let selectedConnId = null;
            let connections = global_1.Global.context.globalState.get(constants_1.Constants.GlobalStateKey);
            if (!connections) {
                vscode.window.showWarningMessage('There are no connections available to rename');
                return;
            }
            if (treeNode && treeNode.connection) {
                selectedConnection = Object.assign({}, treeNode.connection);
                delete selectedConnection.password;
                selectedConnId = treeNode.id;
            }
            else {
                let hosts = [];
                for (const k in connections) {
                    if (connections.hasOwnProperty(k))
                        hosts.push({ label: connections[k].label || connections[k].host, connection_key: k });
                }
                const hostToSelect = yield vscode.window.showQuickPick(hosts, { placeHolder: 'Select a connection', matchOnDetail: false });
                if (!hostToSelect)
                    return;
                selectedConnection = Object.assign({}, connections[hostToSelect.connection_key]);
                selectedConnId = hostToSelect.connection_key;
            }
            const label = yield vscode.window.showInputBox({ prompt: "The display name of the database connection", placeHolder: "label", ignoreFocusOut: true });
            selectedConnection.label = label;
            connections[selectedConnId] = selectedConnection;
            const tree = treeProvider_1.PostgreSQLTreeDataProvider.getInstance();
            yield tree.context.globalState.update(constants_1.Constants.GlobalStateKey, connections);
            tree.refresh();
        });
    }
}
exports.renameConnectionCommand = renameConnectionCommand;
//# sourceMappingURL=renameConnection.js.map