import tippy from 'tippy.js';
import {hideOnEsc, hideOnPopperBlur, hideOthersOnOpen} from './tippy-plugins';

import "tippy.js/dist/tippy.css";

export default function (node, options) {
    const plugins = [hideOnEsc, hideOnPopperBlur, hideOthersOnOpen];
	const _options = options ? { ...options, plugins } : { plugins };
    const instance = tippy(node, _options);
    return{
        update( ){
            instance.setProps()
        },
        destroy(){
            instance.destroy();
        }
    }
}