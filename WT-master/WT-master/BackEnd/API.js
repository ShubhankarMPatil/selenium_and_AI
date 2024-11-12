const URL = "https://api.github.com/users/";
let UserName = "KashyapMavani";

const UserData =
        fetch(URL+UserName)
            .then((data)=> data.json())
            .then((data)=> { 
            let {login, id, avatar_url, html_url, bio, publicrepos, followers,following,created_at,updated_at,followers_url,following_url} = data;
                console.log({login, id, avatar_url, html_url, bio, publicrepos, followers,following,created_at,updated_at,followers_url,following_url}); 
                return {login, id, avatar_url, html_url, bio, publicrepos, followers,following,created_at,updated_at};
            });

// form -> targetvalue -> URL + targetValue -> onCLick = GetUserData    