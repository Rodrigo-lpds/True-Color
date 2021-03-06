# Criação de projeções em composição colorida

## Descrição
O projeto foi criado com o objetivo de utilizar dados geoespaciais (de formato **NetCDF**) dados pelo satélite **GOES-16** para confecção de projeções em composição colorida. A partir dos **16** canais do satélite podemos extrair diferentes tipos de dados, sendo cada canal diferente entre si por estarem em frequencias diferentes.
Neste projeto, usaremos **3** canais de forma simultânea, sendo o canal **1,2 e 3**, para sua confecção.

## Instalação e Ajustes
Para a execução dos scripts que serão mencionados posteriormente, será necessária a instalação de certos programas.

#### Anaconda
Distribuição que nos dará as ferramentas necessárias para uma execução mais prática e direta.
O download da distribuição pode ser encontrado no [site oficial](https://www.anaconda.com), e até o momento por este [link](https://www.anaconda.com/distribution/#download-section).

**Importante: É recomendado que após a instalação completa do Anaconda, seja criado um Ambiente, ou Environment, _específico_ para o projeto.**
#### Spyder
IDE que utilizaremos para plotar as projeções e para debugar os scripts.
As instruções para download podem ser encontradas neste [link](https://docs.spyder-ide.org/installation.html).

Agora será necessário a instalação de pacotes pelo Anaconda. Abra o **Anaconda Prompt** e digite estes comandos no terminal:

Biblioteca para Python e suas dependencias, necessárias para manipulação de dados **NetCDF's**. Para mais informações [acesse](https://anaconda.org/anaconda/netcdf4).
> conda install -c conda-forge netCDF4

Biblioteca **matplotlib basemap** responsável por plotar dados 2D de mapas em Python. Para mais informações [acesse](https://matplotlib.org/basemap/index.html).
> conda install -c conda-forge basemap

Biblioteca parecida com a **PIL**, responsável por auxiliar no processamento de imagens pelo interpretador Python. 
> conda install -c anaconda pillow 

Biblioteca **GDAL** responsável por manipular dados GeoEspaciais
> conda install -c conda-forge gdal

Finalmente, baixe os arquivos netCDF neste [diretório](https://drive.google.com/drive/folders/1IESFYnriP_4ceJuxIxH1GHN9cV4g_CvO?usp=sharing) e os coloque na pasta **samples.**


## Feito isso,após a instalação bem sucedida das bibliotecas e do ambiente o script trueColorRJ_Tutorial pode ser executado em pleno funcionamento. E a projeção abaixo deve ter sido feita!

![TrueColorRJ-02-Apr-2020_13_40_20](https://user-images.githubusercontent.com/56642493/89689233-56442c80-d8da-11ea-8df2-7e4c7990ada0.png)


## Créditos
Script criado por mim: Rodrigo Lucas Pinto da Silva. [Github](https://github.com/Rodrigo-lpds) e [Linkedin](https://www.linkedin.com/in/rodrigo-lucas-pinto-da-silva-3684a8179/)

Usando como referencia o blog: [GEONETClass - Americas](https://geonetcast.wordpress.com) e seus tutoriais que podem ser [encontrados aqui](https://geonetcast.wordpress.com/gnc-a-product-manipulation-tutorials/) no estudo inicial de projeções via NetCDF.

Os tutoriais de [Unidata Python Gallery](https://unidata.github.io/python-training/) para criação de diversos tipos de projecões **True Color** que podem ser [encontrados aqui](https://unidata.github.io/python-gallery/examples/mapping_GOES16_TrueColor.html)

E mentoria teórica geral de **Meteorologia e Dados Via Satélite** por [Fabio Hochleitner](https://www.linkedin.com/in/fabioh/) 
