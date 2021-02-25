
#europe.csv exercice
#Nombre d'heures travaillées par semaine dans les pays U.E
#personnes ayant un emploi à plein temps(Open Data de l'office statistique de l'UE)
#lien de l'Open Data :https://ec.europa.eu/eurostat/web/products-datasets/-/tps00071

#nettoyer les objets et les graphiques 
rm(list=objects())
graphics.off()
europe<-read.table("europe.csv",dec=".",sep=";",quote="",header=TRUE)
#statistiques de base avec summary pour europe
summary(europe)
#6 premières lignes du tableau europe
head(europe)
payseurope<-europe$X.Pays.
#moyenne temps de travail hebdomadaire de tous les pays de l'UE
moydureeue<-mean(europe$X.Durée.heures..)
#med temps de travail hebdomadaire de tous les pays de l'UE
meddureeue<-median(europe$X.Durée.heures..)
#affichage table europe
print(europe)
#affichage colonne pays u.e
print(payseurope)
tempstravaileurope<-europe$X.Durée.heures..
#affichage colonne temps travail u.e
print(tempstravaileurope)
#variance 
var(europe$X.Durée.heures..)#1.23: petite variance 

#temps de travail maximal de europe
maxtempstravail<-max(europe$X.Durée.heures..)
print(maxtempstravail)

#temps minimal de europe
mintempstravail<-min(europe$X.Durée.heures..)
print(mintempstravail)

#étendue de europe
diffheure<-maxtempstravail-mintempstravail
print(diffheure)

#renvoyer les lignes de europe ayant la valeur maximale du temps de travail
subset(europe,X.Durée.heures..==maxtempstravail)
#Les autrichienn.e.s et les grecqu.e.s ont la durée du temps de travail hebdomadaire la plus élevée
#renvoyer les lignes de europe ayant la valeur minimale du temps de travail
subset(europe,X.Durée.heures..==mintempstravail)
#Les lithuanien.nes ont la durée de temps de travail  la plus faible


#faire un damier en faisant une matrice à 2 lignes et 3 écrans
m<-matrix(0:3,nrow=2,byrow=TRUE)
layout(m)
#réglage des marge mar et oma(outer margin area)
par(oma=rep(2,4),mar=rep(2,4))
#boite à moustaches dans la fenêtre plots
boxplot(europe$X.Durée.heures..,ylab="Temps de travail dans l'UE (en heures)", main="Distribution des données")
#afficher points moyenne heures de style triangle
points(1,mean(europe$X.Durée.heures..),pch=2)
payseurope<-europe$X.Pays.
neweuropeclassement<-europe[order(europe$X.Durée.heures..,decreasing=TRUE),]
print(neweuropeclassement)
tempstravaileuropetri<-neweuropeclassement$X.Durée.heures..
#histogramme temps de travail UE avec bordure noire/bleue et couleur des données violette
barplot(europe$X.Durée.heures..,ylim=c(0,50),border="dark blue",col="green",ylab="Temps de travail dans l'UE(en heures)",names.arg=row.names(europe),main="Représentation du temps de travail /pays")
#tracer ligne horizontale au niveau de la moyenne de la durée de travail en couleur orange
abline(h=mean(tempstravaileurope),col="purple")
#histogramme trié par temps de travail décroissant
barplot(neweuropeclassement$X.Durée.heures..,ylim=c(0,50),border="dark blue",col="green",ylab="Temps de travail dans l'UE(en heures)",names.arg=row.names(neweuropeclassement),main="Représentation triée selon la durée du travail")
#tracer ligne horizontale au niveau de la moyenne de la durée de travail en couleur orange
abline(h=mean(tempstravaileuropetri),col="purple")


#données europe classées selon le temps de travail par ordre décroissant
neweuropeclassement<-europe[order(europe$X.Durée.heures..,decreasing=TRUE),]
print(neweuropeclassement)
#extraire pays dont la durée du temps de travail inférieure à la moyenne de temps de travail
inflistepaysmoy<-subset(europe,X.Durée.heures..<moydureeue)
print(inflistepaysmoy)
#nombre de pays en dessous de la moyenne de durée de travail hebdomadaire U.E
nrow(inflistepaysmoy)#15 pays comptabilisés
#extraire pays dont la durée du temps de travail est inférieure à la médiane
inflistepaysmed<-subset(europe,X.Durée.heures..<meddureeue)
print(inflistepaysmed)
#nombre de pays en dessous de la mediane de durée de travail hebdomadaire U.E
nrow(inflistepaysmed)#12 pays comptabilisés
