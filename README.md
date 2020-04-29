# Rocket League Replay Map Changer
Changes the map on a Rocket League replay

## Requirements
* Windows
* Python 3.6+
* Tqdm Library
* Requests Library

## Dependencies
RLMapChanger utilizes the [Rattletrap](https://github.com/tfausak/rattletrap) Rocket League replay parser because of its ability to both decode and encode replays. This parser is downloaded automatically upon running the script.

The tqdm library to visualize conversion progress of a directory and can be installed by running:

    pip install tqdm

The requests library is used to retireve the latest [Rattletrap](https://github.com/tfausak/rattletrap) parser release and can be installed by running:

    pip install requests

Both libraries can be installed simultaneously using the ```requirements.txt``` file by running:

    pip install -r requirements.txt


## Interface
Argument|Type|Description
:---|:---:|---:
-r --replay|PATH|Path of the replay to convert
-d --replay-directory|PATH|Directory of the replays you wish to convert
-m --map|STRING|Map code of the map you wish to convert to
-v --verbose|BOOL|Increased output verbosity

## Usage
To run the script with a single replay file:

    python MapChanger.py -r "Path/to/replay/file" -m "map_code"

To run the script for a replay directory:

    python MapChanger.py -d "Path/to/replay/directory/" -m "map_code"

To enable verbose output, append the `-v` argument


## Map Documentation
Each map has a shorthand value used by Rocket League. To specifiy a map, run the script using the shorthand value as defined below:

    {
        "arc_p": "Starbase ARC",
        "arc_standard_p": "Starbase ARC (Standard)",
        "beach_night_p": "Salty Shores (Night)",
        "beach_p": "Salty Shores",
        "beachvolley": "Salty Shores (Volley)",
        "chn_stadium_p": "Forbidden Temple",
        "cs_day_p": "Champions Field (Day)",
        "cs_hw_p": "Rivals Arena",
        "cs_p": "Champions Field",
        "eurostadium_night_p": "Mannfield (Night)",
        "eurostadium_p": "Mannfield",
        "eurostadium_rainy_p": "Mannfield (Stormy)",
        "eurostadium_snownight_p": "Mannfield (Snowy)",
        "farm_night_p": "Farmstead (Night)",
        "farm_p": "Farmstead",
        "farm_upsidedown_p": "Farmstead (The Upside Down)",
        "haunted_trainstation_p": "Urban Central (Haunted)",
        "hoopsstadium_p": "Dunk House",
        "labs_circlepillars_p": "Pillars",
        "labs_cosmic_p": "Cosmic",
        "labs_cosmic_v4_p": "Cosmic",
        "labs_doublegoal_p": "Double Goal",
        "labs_doublegoal_v2_p": "Double Goal",
        "labs_octagon_02_p": "Octagon",
        "labs_octagon_p": "Octagon",
        "labs_underpass_p": "Underpass",
        "labs_underpass_v0_p": "Underpass",
        "labs_utopia_p": "Utopia Retro",
        "neotokyo_p": "Neo Tokyo",
        "neotokyo_standard_p": "Neo Tokyo (Standard)",
        "park_night_p": "Beckwith Park (Midnight)",
        "park_p": "Beckwith Park",
        "park_rainy_p": "Beckwith Park (Stormy)",
        "shattershot_p": "Core 707",
        "stadium_day_p": "DFH Stadium (Day)",
        "stadium_foggy_p": "DFH Stadium (Stormy)",
        "stadium_p": "DFH Stadium",
        "stadium_winter_p": "DFH Stadium (Snowy)",
        "throwbackstadium_p": "Throwback Stadium",
        "trainstation_dawn_p": "Urban Central (Dawn)",
        "trainstation_night_p": "Urban Central (Night)",
        "trainstation_p": "Urban Central",
        "underwater_p": "Aquadome",
        "utopiastadium_dusk_p": "Utopia Coliseum (Dusk)",
        "utopiastadium_p": "Utopia Coliseum",
        "utopiastadium_snow_p": "Utopia Coliseum (Snowy)",
        "wasteland_night_p": "Wasteland (Night)",
        "wasteland_night_s_p": "Wasteland (Standard, Night)",
        "wasteland_p": "Wasteland",
        "wasteland_s_p": "Wasteland (Standard)"
    }