if exist mars-rover-team\ (
    cd mars-rover-team
    git pull
    cd ..
) else (
    git clone https://github.com/bramvandermeersch/mars-rover-team.git
)

python mars-rover-team\src\run_rover.py
pause