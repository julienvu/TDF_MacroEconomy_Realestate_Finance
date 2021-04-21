
# données sources: organisme Fred https://fred.stlouisfed.org/
#debut code R
#donnees fichier excel database-reaction_function2020.xlsx
#importation des libraries readxl, dplyr, stats
library(readxl)
library(dplyr, quietly = TRUE)
library(stats)

#suppression des variables d'environnement de la mémoire
remove(list = ls())

#importation fichier excel données sources
database_reaction_function2020 <- read_excel("Master_Info_Dauphine/M2_ID/database-reaction_function2020.xlsx")
View(database_reaction_function2020)
head(database_reaction_function2020)
df1 <-database_reaction_function2020[,-10]

#suppresion des colonnes après la colonne ib
df1 <-df1[,-11]
#df1 <-df1[,-12]
df1 <-df1[,-11]
df1 <-df1[,-10]
names(df1)[1] 
names(df1)[3]
names(df1)
View(df1)

#remplacer nom de colonne ...1 par date
dfinal <-df1%>% rename(date = ...1)
names(dfinal)[1]#"date" 
names(dfinal)[3]#"rb"
names(dfinal)[8]#"if"

#renommage colonne 8 if par inflafrance
names(dfinal)[8]<-"inflafrance"

#voir table modifiée
View(dfinal)

#tracer des séries temporelles pour taux d'intérêt(BDF, bundesbank, Fed et général)
plot(dfinal$date,dfinal$rf,col="purple",type="l", main="Taux d'intérêt en fonction du temps", xlab = "date",ylab="taux d'intêret rf/rb/ru/général")
lines(dfinal$date,dfinal$rb,col="orange")
lines(dfinal$date,dfinal$ru,col="blue")
lines(dfinal$date,dfinal$rdb, col="green")
# Add a legend pour taux d'intérêt
legend("right", legend=c("rf", "rb","ru","rdb"),
       col=c("purple", "orange","blue","green"), lty=1:2, cex=0.8)

#tracer des séries temporelles pour taux de change
#fenêtre 1*2 graphique
par(mfrow=c(1,2))
plot(dfinal$date,dfinal$ff,col="brown",type="l",main="Tchange ff", xlab = "date",ylab="taux de change ff")
# Add a legend pour taux de change ff
legend("topleft", legend=c("ff"),
       col=c("brown"), lty=1:2, cex=0.8)
plot(dfinal$date,dfinal$dm,col="orange",,type="l",main="Tchange dm", xlab = "date",ylab="taux de change dm")
# Add a legend pour taux de change dm
legend("topleft", legend=c("dm"),
       col=c("orange"), lty=1:2, cex=0.8)

#tracer des séries temporelles pour taux d'inflation
#retour à la fenêtre normal (1*1)
par(mfrow=c(1,2))
plot(dfinal$date,dfinal$ib,col="blue",type="l",main="Tinflation en fonction du temps", xlab = "date",ylab="taux d'inflation")
legend("topright", legend=c("ib"),
       col=c("blue"), lty=1:2, cex=0.8)
plot(dfinal$date,dfinal$inflafrance,col="pink",type="l",main="Tinflation en fonction du temps", xlab = "date",ylab="taux d'inflation")
# Add a legend pour taux d'inflation
legend("topright", legend=c("inflafrance"),
       col=c("pink"), lty=1:2, cex=0.8)

#voir les corrélations entre certaines variables du jeu de données
#coefficient de corrélation de pearson avec complete.obs qui supprime les lignes 
#contenant des valeurs manquantes
cor(dfinal$rf,dfinal$inflafrance,use="complete.obs")#
#interprétation :corrélation positive très forte entre les deux variables

cor(dfinal$rb,dfinal$ib,use="complete.obs")#0.946854 très proche de 1
#interprétation :corrélation positive très forte entre les deux variables

#taux intérêt allemagne et taux d'inflation allemagne
cor(dfinal$rf,dfinal$ff,use="complete.obs")#0.04 très proche de 0
#aucune relation entre le taux d'intérêt france et le taux de change france
cor(dfinal$rb,dfinal$dm,use="complete.obs")#0.06382578 très proche de 0
#aucune relation entre le taux d'intérêt allemagne et le taux de change allemagne

cor(dfinal$rf,dfinal$rdb,use="complete.obs")#0.7694166 très proche de 1
#interprétation :corrélation positive forte entre les deux variables
#taux intérêt france et taux d'intérêt général

cor(dfinal$rb,dfinal$rdb,use="complete.obs")#0.7694166 très proche de 1
#interprétation :corrélation positive très forte entre les deux variables
#taux intérêt allemagne et taux d'intérêt général

cor(dfinal$ff,dfinal$rdb,use="complete.obs")#-0.3348911 négatif
#valeur négative du coefficient et relation non linéaire entre les deux variables
#taux de change france et taux d'intérêt général

cor(dfinal$dm,dfinal$rdb,use="complete.obs")#0.06976173 proche de 0
#valeur du coefficient et relation non linéaire entre les deux variables
#taux de change allemagne et taux d'intérêt général

cor(dfinal$inflafrance,dfinal$rdb,use="complete.obs")#0.8801829 valeur proche de 1
#interprétation :corrélation positive très forte entre les deux variables
#taux d'intérêt général et taux d'inflation france

cor(dfinal$inflafrance,dfinal$ff,use="complete.obs")#-0.376904 négatif
#sens de relation non linéaire entre les variables
#taux d'inflration france et taux de change france

cor(dfinal$ib,dfinal$rdb,use="complete.obs")#0.8920401valeur proche de 1
#interprétation :corrélation positive très forte entre les deux variables
#taux d'intérêt général et taux d'inflation allemagne


cor(dfinal$ib,dfinal$dm,use="complete.obs")
#0.03744707 très proche de 0 mais positif
#valeur très proche de 0 et relation non linéaire entre les deux variables
#taux de change allemagne et taux d'inflation allemagne


#Amplitude des variables du jeu de données
#taux intérêt france gap max min
print('étendue taux intérêt france: ')
max(dfinal$rf)-min(dfinal$rf)#12.375

#taux intérêt allemagne gap max min
print('étendue taux intérêt allemagne: ')
max(dfinal$rb)-min(dfinal$rb)#8.5

#taux intérêt fed gap max min
print('étendue taux intérêt fed: ')
max(dfinal$ru)-min(dfinal$ru)#13.25

#taux change france gap max min
print('étendue taux de change france: ')
max(dfinal$ff)-min(dfinal$ff)#6.0528

#taux change allemagne gap max min
print('étendue taux de change allemagne: ')
max(dfinal$dm)-min(dfinal$dm)#1.669

#taux intérêt général gap max min
print('étendue taux intérêt général: ')
max(dfinal$rdb)-min(dfinal$rdb)#5

#taux inflation allemagne gap max min
print('étendue taux d inflation allemagne: ')
max(dfinal$inflafrance)-min(dfinal$inflafrance)#12.43

#taux inflation allemagne gap max min
print('étendue taux d inflation allemagne: ')
max(dfinal$ib)-min(dfinal$ib)#8.46


#regression lineaire multiple avec l'instruction lm entre taux intérêt france en fonction
#du taux intérêt allemand, taux intérêt américain et taux inflation france

tauxintfrreg<-lm(dfinal$rf ~ dfinal$rb +dfinal$ru+dfinal$inflafrance, data=dfinal)
#output regression tauxintffreg
summary(tauxintfrreg)
#Plus la valeur du R ajusté est proche de 1,
#et plus l'adéquation entre le modèle et les données observées va être forte. Cependant, cette valeur est fortement influencée, entre autres
#par le nombre de variables explicatives incluses dans la regression. 

#equation droite
#tauxinteretfrancais= 4.73 +0.57*tauxinteretallemagne-0.21*tauxinteretamericain+ 0.35*tauxinflationfrance
#gamma= 4.73
#coefficients non significatifs pour ru car pas de symbole
#pour rb et inflafrance: significatifs( 90 % et 99,999%)
#avec le taux d'intérêt allemand augmenté de 1% augmente le taux d'intérêt francais de 0.57
#avec le taux d'inflation français augmenté de 1% augmente le taux d'intérêt francais de 0.35
#autre interprétation: pour un taux d'inflation constant, vu que coefficient associé à taux intérêt
#allemand positive, augmenter taux d'intérêt allemand revient donc à augmenter à augmenter taux d'intérêt francais
# stratégie européenne
# Extraction des coefficients
coef(tauxintfrreg)
# Intervalle de confiance (à 95%) des coefficients
confint(tauxintfrreg)
# plot : "vraies" valeurs et droite de regression
plot(dfinal$rf ~ dfinal$rb + dfinal$ru + dfinal$inflafrance, data=dfinal)
abline(tauxintfrreg, col = "orange") 
# Prédiction du taux d'intérêt francais à 99% en fonction du taux d'intérêt allemand, du taux d'intérêt américain et du taux d'inflation francais
valeurspredites <- predict(tauxintfrreg,data.frame(4,3.4,7), level= 0.99)
#Affichage des valeurs prédites du taux d'intérêt francais en fonction du temps
plot(dfinal$date,valeurspredites,col="brown",type="l", main="Prédiction du taux d'intérêt francais")

#fin code R

