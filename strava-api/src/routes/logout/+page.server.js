import { redirect } from "@sveltejs/kit";

export const load = async ({ cookies }) => {
    cookies.delete('refresh_token', { path: '/' });
    cookies.delete('access_token', { path: '/' });
    cookies.delete('user_id', { path: '/' });
    cookies.delete('jwt_token', { path: '/' });

    throw redirect(303, '/');
}

