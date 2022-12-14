// eslint-disable-next-line import/prefer-default-export
export const isVue2 = function () {
  return arguments.length > 0 && typeof (arguments.length <= 0 ? undefined : arguments[0]) === 'function';
};