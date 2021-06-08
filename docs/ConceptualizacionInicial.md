# Contexto

El documento ```ClimaModelosSesgo.pdf``` -en el OneDrive- presenta de forma resumida el problema general de la evaluación de impactos climáticos. El resumen es que para poder evaluar los efectos del cambio climático, necesitamos utilizar los resultados generados por los modelos climáticos. Estos resultados son lo que llamaremos pronósticos climáticos, que son los que queremos analizar para determinar cuál es la señal del cambio climático y qué errores sistemáticos y aleatorios presenta cada modelo.

Para construir un idioma común, que nos asegure que nos basamos en las mismas representaciones y que llamamos a las cosas de la misma forma, retomo la lista de conceptos que propusiste e intento darle una primera iteración a su definición.

# Definiciones

## Modelo climático - $\mathbb{F}_k$

Conjunto de ecuaciones diferenciales deterministas que representan las dinámicas atmosféricas y que se utilizan para generar pronósticos climáticos. Los hay globales que resuelven todo el globo con una resolución grosera -100 km-, los hay regionales, que utilizan los resultados de los globales como condiciones de contorno y resuelven regiones -Europa, por ejemplo- a una mejor resolución -10 km-, y los hay locales, que utilizan la información de los regionales como condición de contorno y resuelven áreas concretas -Cantabria, por ejemplo- con una resolución fina -1km-.

Las escalas a que pueden resolverse las ecuaciones -el tamaño de la malla de resolución- suelen ser groseras respecto a las escalas naturales de los procesos a resolver. Por ello, muchos procesos no pueden resolverse adecuadamente con las ecuaciones basadas en primeros principios. Para solventar este inconveniente, se recurre a submodelos -ecuaciones efectivas- que parametrizan los comportamientos en escalas inferiores a la de la malla de cálculo. Estas ecuaciones efectivas, y sus parametrizaciones, no son únicas, así que se convierten en una decisión de diseño de cada modelo concreto.

Unos modelos climáticos se diferencian de otros por la elección de sus ecuaciones -si bien, las ecuaciones físicas básicas son compartidas-, sus esquemas numéricos y sus esquemas de incorporación de las observaciones. Esto hace que, si bien todos los modelos intentar aproximar las mismas dinámicas, cada uno se ajuste mejor a la reproducción de unas dinámicas o a la captura de la señal en una zona concreta del globo.

Los modelos climáticos son muy complejos y pesados de ejecutar, por lo que queda fuera de nuestras posibilidades el poderlos ejecutar y generar pronósticos por nuestra cuenta. La idea es utilizar los pronósticos generados por la gente que trabaja con los modelos.

## Escenarios climáticos - $\mathbb{RCP}_R$

El cambio climático es un proceso muy complejo que no comprendemos del todo bien. Más aún, siendo un fenómeno antrópico, depende fuertemente de la evolución socio-económica del mundo. Por tanto, pronosticar la evolución del cambio climático requiere pronostica la evolución socio-económica, lo que es altamente complicado.

Esta complicación, añadida al hecho de que los modelos climáticos son modelos deterministas, hace necesario generar **escenarios climáticos** para explorar posibles trayectorias del sistema climático. Estas trayectorias se caracterizan a través de lo que se conoce como **Sendas de concentración representativas (Representativa Concentration Pathways, RCP)**. Los RCP determinan la evolución del forzamiento radiativo -cuanta radiación va a quedar atrapada en el sistema Tierra por efecto invernadero- y constituyen una condición de contorno para los modelos climáticos. Existen 4 RCPs: RCP2.6, RCP4.5, RCP6 y RCP8.5. Los números indican el incremento de forzamiento radiativo medio (en $W/m^2$) sobre todo el globo a final de siglo.

Estos escenarios climáticos son lo más parecido que encontramos dentro del mundo de los modelos climáticos a un muestreo de las predicciones de los modelos climáticos. Pero claro, son cuatro escenarios, es decir, que para una variable, localización y tiempo dados, tenemos únicamente 4 valores predichos por nuestro modelo.

## Pronóstico climático - $C_{krij}(t)$

Los pronósticos climáticos son los resultados obtenidos al integrar las ecuaciones de un modelo climático $\mathbb{F}_k$. Estos resultados toman la forma de matrices que contienen el valor de la variable $i$ en cada localización $j$ de la malla de resolución para el RCP $r$. Existe una matriz por cada paso de tiempo. Esta es la información a la que realmente vamos a tener acceso. Como los modelos $\mathbb{F}_k$ son deterministas, para cada escenario climático $r$ cada modelo $k$ genera un único pronóstico. Es decir, la variable $i$ en la celda $j$ toma un valor único en tiempo $t$.

Si entendí correctamente en la reunión, vamos a necesitar un **modelo generador, $\mathbb{G}$** para poder realizar el análisis de sistemáticos. Como la utilización de los modelos climáticos $\mathbb{F}_k$ queda fuera de nuestro alcance, entiendo que sería necesario formular un modelo estocástico o estadístico que ajuste los datos del pronóstico $C_{krij}(t)$ y que nos permita generar _muestras equivalentes_. No llego aún a vislumbrar si $\mathbb{G}$ ha de aproximar únicamente un $C_{krij}(t)$, o si puede abarcar los pronósticos de varios modelos, distintas variables y en más de una localización. Aquí podrían explotarse propiedades como la estacionalidad, el comportamiento cíclico del clima de periodo un año, para transformar el pronóstico determinista en un objeto con un cierto carácter estadístico, pero aún me falta por comprender bien el procedimiento para poder aportar algo más útil.

## Observaciones meteorológicas - $M_{ij}(t)$

Las observaciones meteorológicas[^1] son las medidas que realizamos para una variable $i$ en una localización $j$ en un tiempo $t$. Un ejemplo sería una lectura de un termómetro. Es importante notar aquí que para una misma localización $j$ de la malla de cálculo de un modelo, puedo tener varias medidas para una misma variable. En una malla de 10 km x 10 km que cubriese Santander, podría tener un valor del termómetro del Aeropuerto, otro en las oficinas de AEMET, en la Maruca, y otro en lo alto de Peña Cabarga. Como cada localización tiene sus características -unas miran al sur, otras al norte, otras están en altura- las medidas van a diferir unas de otras, y sólo tiene sentido compararlas con los pronósticos climáticos $C_{krij}(t)$ en términos estadísticos. Es importante señalar que existe un periodo de referencia -1980-2010- para el que todos los escenarios $r$ aportan la misma información, por lo que en ese periodo sólo existe un pronóstico y no los 4 asociados a cada RCP.

[^1]: La meteorología hace referencia a los valores instantáneos de las variables atmosféricas, mientras que la climatología es el estudio de las propiedades estadísticas de dichas variables. Suele decirse que el tiempo atmosférico -la temperie- dicta la ropa que me pongo un día concreto, mientras que el clima condiciona la ropa que tengo en el armario.

## Modelos proyectivos - $Pm_{krij}(t)$

Si entiendo bien este concepto, los modelos proyectivos serían el _algoritmo_ que a partir de los $C_{krij}(t)$ produce una estimación $\hat{M}_{krij}(t)$ de las observaciones $M_{ij}(t)$. Si esto es correcto, entonces los **modelos proyectivos** serían las _técnicas de corrección de sesgo_ o de _reducción de escala (downscaling)_. En el documento ```ClimaModelosSesgo.pdf``` tienes una pequeña introducción. También encontrarás dos papers de Maraun y otro de Gutiérrez que presentan lo más actual sobre el tema.

Es importante hacer hincapié sobre el hecho de que estos **modelos proyectivos** no aprovechan la información más que de un único modelo. Una vez que se han generado las estimaciones $\hat{M}_{krij}(t)$ para cada modelo, no existen -hasta donde yo tengo conocimiento- procedimientos robustos para generar una estimación $\hat{M}_{ij}(t)$ que marginalice la variable modelo. A veces se recurre a medias ponderadas, donde los pesos son inversamente proporcionales al error cuadrático medio de la aproximación de cada modelo a una variable concreta. Este sería el punto clave dónde podría encajar nuestra contribución -un esquema proyectivo que permita aprovechar la información de cada modelo de la mejor forma posible-.

## Distribución de cambio climático - $S_{ij}(t)$

La definición de la distribución $S_{ij}(t)$ de cambio climático es un poco complicada en el sentido siguiente. Cada modelo climático $\mathbb{F}_k$ genera unos pronósticos $C_{krij}(t)$, es decir, genera una serie temporal única por cada escenario RCP $r$. Por tanto, cada modelo aproxima la distribución en un determinado instante a partir de 4 valores, que corresponden a los RCP utilizados. Por tanto, si bien es totalmente razonable asumir que existe una distribución $S_{ij}(t)$ que caracteriza el efecto del cambio climático, un único modelo la aproxima de una forma **muy pobre**, puesto que sólo aporta 4 muestras de la misma.

Ahora bien, efectivamente, de forma colectiva, los pronósticos $C_{krij}(t)$ sí puede considerarse que aproximan la distribución subyacente $S_{ij}(t)$. Es decir a partir de $C_{krij}(t)$ puedo construir una  $\hat{S}_{ij}(t)$ que aproxima $S_{ij}(t)$. Sin embargo, aquí es donde entran los posibles errores sistemáticos y aleatorios de cada modelo.

Por tanto, parece totalmente razonable asumir que existe una distribución $S_{ij}(t)$ de cambio climático independiente del modelo ($k$) y del escenario ($r$), pero no está claro que un único modelo sea una buena aproximación de la misma. Sí podría serlo si en lugar de considerar $S_{ij}(t)$ como una distribución que varía de forma continua en el tiempo, la considerásemos en otros periodos de agregación, por ejemplo $S_{ij}\{m\}$ como la distribución de cambio climático para el mes $m$.

## Distribución real - $PS_{ij}(t)$

Efectivamente, de la misma manera que los distintos modelos $\mathbb{F}_k$ definen una distribución de cambio climático $S_{ij}(t)$ que está ligada a sus resoluciones espaciales y temporales, podemos asumir que existe una distribución $PS_{ij}(t)$ que captura el efecto que el cambio climático tiene sobre las observaciones $M_{ij}(t)$. Puede existir una dificultad en este caso debida al hecho de que, como mencioné antes, $M_{ij}(t)$ no es un valor único, sino que podemos tener varias observaciones $M^{\alpha}_{ij}(t)$ en varios puntos dentro de $j$, y por tanto, quizá tendríamos una distribución distinta por punto de observación $PS^{\alpha}_{ij}(t)$.

Estas distribuciones reales estarían ligadas a los modelos proyectivos, ya que de la misma forma que transforman los pronósticos $C_{krij}(t)$ en una estimación $\hat{M}_{krij}(t)$ de las observaciones $M_{ij}(t)$, deberían transformar la distribución $S_{ij}(t)$ en una estimación $\hat{PS}_{ij}(t)$ de $PS_{ij}(t)$.

# Objetivo

Una vez _formalizados_[^2] estos conceptos, podríamos describir dos objetivos para este trabajo.

1. Dados unos pronósticos $C_{krij}(t)$ de los modelos $\mathbb{F}_k$, determinar la distribución $S_{ij}(t)$ que definen, en principio sin hacer uso de las observaciones $M_{ij}(t)$, lo que no sé si será posible.
2. Dados unos pronósticos $C_{krij}(t)$ de los modelos $\mathbb{F}_k$, determinar la distribución $PS_{ij}(t)$ que definen, haciendo uso de las observaciones $M_{ij}(t)$.

En ambos casos, tratando de manera robusta los errores sistemáticos $\vert C_{krij}(t) - S_{ij}(t) \vert$ para $t < t_o$ y $\vert Pm_{krij}(t) - PS_{ij}(t) \vert$ para $t < t_o$ y potencialmente combinando los modelos para mejorar la predicción.

El primero objetivo es interesante puesto que pretendería aprender, únicamente a través de los pronósticos de los modelos, cuál es la señal de cambio climático que daría el _modelo ideal_. Esto permitiría generar unos pronósticos _únicos_ donde el analista no climatólogo, podría olvidarse de modelos y escenarios, y acudir a los datos de un modelo _único_ con los que trabajar.

El segundo objetivo cambia ligeramente según el primer objetivo sea realizable o no. Si el primer objetivo es realizable, el segundo objetivo perseguiría encontrar la transformación óptima desde el _modelo ideal_ hasta mis observaciones. Si el primer objetivo no es realizable, el segundo perseguiría definir el _modelo ideal_ para una variable concreta en una localización concreta considerando una observación concreta. Es decir, sería un objetivo mucho menos general.

[^2]: Obviamente esta formalización probablemente tenga que mejorar, pero quiero asumir que puede ser un punto de partida aceptable.