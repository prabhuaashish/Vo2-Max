export const load = async ({ locals, cookies }) => {
    if (locals.user) {
        cookies.set('user_id', locals.user.id, { path: '/' });
    }
        
    return {
        user: locals.user
    };
}
