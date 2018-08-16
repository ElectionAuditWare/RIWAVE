[![CircleCI](https://circleci.com/gh/zperumal/RIWAVE.svg?style=svg)](https://circleci.com/gh/zperumal/RIWAVE)
# Rhode Island Wave
A mathematically hot-swappable audit station designed for conducting RLA's in 
Rhode Island.

# Execution Directions

Go to [releases](https://github.com/agupta231/RIWAVE/releases) and download the latest
version relevant to your platform. 

## Windows

Download the compressed file that starts with `windows_`. Unzip the file and double click
the `Audit Station` executable in the folder.

## macOS

Download the compressed file that starts with `mac`. Unzip the file. Open
`/Applications/Utilities/Terminal.app/`. In Terminal, type in `cd` and drag the folder into
the Terminal. Your terminal should look something like `cd 
/Users/test_user/Downloads/mac_RI_special`. Press enter. Type `./audit_station` and press
enter.

## Linux

Download the compressed file that starts with `linux`. Unzip the file and run the executable
`audit_station`. This is known to work on Fedora 28. If the executable doesn't work on your
distribution, then you may need to build from sources. See below for futher instructions.

# For Developers
This project is built using **Python 3**. 

If you already have pip installed (Just try running `pip` from the command line), simply 
run `pip install -r requirements.txt`. 

If not, then you will have to install `pip`. You can either just install `pip` by itself,
but we recommend installing `anaconda`, which will sandbox your python installation so that
it won't interfere with anything else on your system. 

Install `anaconda` for your respective operating system by [following this](https://conda.io/docs/user-guide/install/index.html#regular-installation). Once `conda` is installed, create a new conda environment that
 uses `python 3` and `pyqt 5`. For most systems, this is done by `conda create --name
 riwave python=3 pyqt=5`

After the environment has been properly set up, run `source activate riwave` to activate
the environment. You should see a `(riwave)` on the very left of your prompt.

Whether or not you installed `anaconda` or just `pip` by itself, run `python __main__.py` 
in the `WAVE` folder to begin the audit station.

# In Program Use
In this section, the use of the audit station will be described. This section will use the
example of RI special election, which can be used by running `python __main_RI_Election.py`.

## Seed Generation
When you first run the application, you will be greeted with a seed generation screen, as
shown below:

![Seed Generation][seed_gen]

Type in the random seed, which can be generated via dice or any other method of choosing, to
generate the order in which ballots are audited. Then, press **confirm** and **save**. The
main window will pop up, and the seed generation window can be safely closed.

## Auditing
Once you finish up on the seed generation, you will be greeted with the main audit station:

![Main Audit Station][station_main]

### Audit Station Setup

The audit station is split into 5 main parts, explained below.

#### Audit Record Table

![Audit Record Table][station_audit_table]

The audit record table shows all of the ballots that have already been audited. Each ballot
is its own row, and has four attributes to it:

* **Audit #** is an indexing of the ballot
* **Actual Ballot #** is what the ballot is labeled in real life. For example, if the **actual ballot #** was 49, then the ballot labeled as 49 would be picked up.
* **Reported Value** is what the machine (or CVR) interpretation of the ballot
* **Actual Value** is the human interpretation of the ballot

#### Election Details

![Election Details][station_ele_details]

Here, the user can see the details of what they are auditing. As shown in the image, the
**contestants** section has 2 sections: 

* The internal indexing of each contestant. This is for the convenience of a 3rd party
  auditor who may want to look under the hood at the mathematical workings.
* The name of the contestant

Additionally, the auditor can see the **reported results** of the election, and verify that
everything is how it is supposed to be:

#### Current Ballot

![Current Ballot Details][station_current_ballot]

This is the information for the current ballot. Here, the user can correct the information
from a CVR and input the "correct" value for the ballot. The **save** button will update the
information on the current ballot and recompute the audit. The **save and continue** button
will do everything the save button does, and choose the next ballot to be audited.

*Note:* Any ballot that is clicked in the [Audit Record](#audit-record-table) will have its
information reflected in the current ballot section.

#### Progress

![Progress][station_progress]

Here, the user can see the current status of the audit. The value shown is the math that is
relevant to the audit, whether it is the T value in a Ballot Polling RLA or the number of
ballots left in a Comparison RLA. While the audit is running, there are three status codes
that reflect the state of the audit: `Audit Complete`, `In Progress`, or `Full Recount
Required`.

#### Audit Details

![Audit Details Section][station_audit_details]

Here, the user can configure the audit and change the different hyper parameters associated
with the audit. If the user wants to mess with the current audit, they simply just adjust
the values in the table and press **recompute**. 

If the user wishes to change the audit, they can use the switcher to switch out audits. 
Then they press **recompute**. This will update the table of parameters so the user can
tweak them to their desire. Once the parameters are set, the user just presses **recompute**
once more to run the audit on the previously selected ballots.

### Running the Audit

Running the audit is simple. Simply press the **Save and Continue** button and correct the
current ballot's actual value. The station will alert the user when the audit is finished.

#### Switching Audits

If the user switches the audit, there is a chance that the number of audited ballots was too
high for the new audit. For example, a Ballot Polling RLA might need 100 ballots, while a 
comparison RLA may only need 20. If this type of situation occurs, when the audit is
recompute, the last ballot to be used in the computation will be highlighted to indicate
where the audit had stopped, as shown below:

![Last Ballot Audited][last_ballot]


[seed_gen]: https://imgur.com/25G2mwG.png "Seed Generation"
[station_main]: https://imgur.com/MpwTU5B.png "Main Screen"
[station_audit_table]: https://imgur.com/kz6U8dQ.png "Audit Table"
[station_ele_details]: https://imgur.com/92cT38l.png "Election Details"
[station_current_ballot]: https://imgur.com/HJEAIs5.png "Current Ballot"
[station_progress]: https://imgur.com/Mgviij9.png "Progress"
[station_audit_details]: https://imgur.com/ckT2KtO.png "Audit Details"
[last_ballot]: https://imgur.com/5n2b5sJ.png "Switching Settings"
