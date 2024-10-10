const URL = "https://api.github.com/users/";

        async function getUserData() {
            const username = document.getElementById("usernameInput").value;
            const userData = await fetch(URL + username)
                .then(response => response.json())
                .then(data => {
                    return {
                        login: data.login,
                        id: data.id,
                        avatar_url: data.avatar_url,
                        html_url: data.html_url,
                        bio: data.bio,
                        public_repos: data.public_repos,
                        followers: data.followers,
                        following: data.following,
                        created_at: data.created_at,
                        updated_at: data.updated_at
                    };
                })
                .catch(error => {
                    console.error("Error fetching user data:", error);
                    return null;
                });

            if (userData) {
                displayUserData(userData);
            }
        }

        function displayUserData(userData) {
            const userInfoDiv = document.getElementById("user-info");
            const userAvatarDiv = document.getElementById("user-avatar");
            const userDetailsDiv = document.getElementById("user-details");

            userInfoDiv.style.display = "block";
            userAvatarDiv.innerHTML = `<img src="${userData.avatar_url}" alt="User Avatar">`;
            
            userDetailsDiv.innerHTML = `
                <p id="username_element"><strong>Username:</strong> ${userData.login}</p>
                <p><strong>Bio:</strong> ${userData.bio || "N/A"}</p>
                <p><strong>Public Repositories:</strong> ${userData.public_repos}</p>
                <p><strong>Followers:</strong> ${userData.followers}</p>
                <p><strong>Following:</strong> ${userData.following}</p>
                <p><strong>Profile URL:</strong> <a href="${userData.html_url}" target="_blank">${userData.html_url}</a></p>
                <p><strong>Account Created:</strong> ${new Date(userData.created_at).toLocaleDateString()}</p>
                <p><strong>Last Updated:</strong> ${new Date(userData.updated_at).toLocaleDateString()}</p>
            `;
        }