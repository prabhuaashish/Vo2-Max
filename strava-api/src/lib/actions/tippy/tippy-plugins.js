import { hideAll } from 'tippy.js';

export const hideOnPopperBlur = {
    name: 'hideOnPopperBlur',
    defaultValue: true,
    fn(instance) {
      return {
        onCreate() {
          instance.popper.addEventListener('focusout', (event) => {
            if (
              instance.props.hideOnPopperBlur &&
              event.relatedTarget &&
              !instance.popper.contains(event.relatedTarget)
            ) {
              instance.hide();
            }
          });
        },
      };
    },
};

export const hideOnEsc = {
    name: 'hideOnEsc',
    defaultValue: true,
    fn({hide}) {
      function onKeyDown(event) {
        if (event.keyCode === 27) {
          hide();
        }
      }
  
      return {
        onShow() {
          document.addEventListener('keydown', onKeyDown);
        },
        onHide() {
          document.removeEventListener('keydown', onKeyDown);
        },
      };
    },
};

export const hideOthersOnOpen = {
	name: 'hideOthersOnOpen',
	defaultValue: true,
	fn(instance) {
		return {
			onShow() {
				hideAll({ exclude: instance });
			}
		};
	}
};