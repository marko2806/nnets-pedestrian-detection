# Priprema repozitorija

Za početak je potrebno klonirati ovaj repozitorij.
Zatim unutar ovog repozitorija klonirati https://github.com/ultralytics/yolov5.git repozitorij.
Sa google drivea preuzeti dataset i kopirati ga u root repozitorija.

Link na google drive sa datasetom:
#TODO

Struktura bi nakon ova trebala izgledati ovako:
* nnets-pedestrian-detection
    * exp36
    * config
    * yolov5
        * data
        * runs
            * train
        * ...
    *  dhd_campus_new
        * train
        * val
        * test
  

Direktorij *exp36* kopirati u *yolov5/runs/train*
Datoteke u direktoriju *config* prekopirati u *yolov5/data*

# Analiza podataka

Za analizu podataka pozicionirati se u mapu repozitorija (mapa *nnets-pedestrian-detection*) i pokrenuti naredbu:

*tensorboard --logdir yolov5/runs/train*

Na https://localhost:6006 će se pokazati svi grafovi vezani u treniranje.
