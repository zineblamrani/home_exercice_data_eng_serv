# Project servier

## Assumptions

We use pyenv (to manage python versions) and poetry (for package dependencies management).
We use python 3.12.7.

## Installation

```bash
pyenv local 3.12.7  # set local python version to 3.12.7
poetry install  # install project depedencies
poetry shell  # jump in the project virtual env
```

## Tests

We use pytest for our test framework

```bash
pytest tests/
```

## Run

Run the following command:

```bash
python run.py
```

And checkout the result in the following output file:

```bash
ls -al outputs/references.json
jq '.' outputs/references.json
```

## Implementation logic

* In this project we need to load different data sources (drugs, pubs, trials) and we need to build a target dataset which reconciles relationships between each of these entities.
* We have split our code to reflect these steps (sources, transformation, targets).
* In sources we define the specificies to load each input dataset in a declarative way.
* In transformations we take the sources as input arguments and we creates the relationships between drugs, pubs, trials and journals.
* In targets we take the transformations dataset and we format it based on the expected output and we write it down in json.

Because we have been ask to create this project as it was a team project, we have also set in places couples of good practices:

* We are using pytest for the test framework and all tests are under tests/ coverage is not around 100% because of the time constraint but we tried to showed different test patterns.
* We also added a pre-commit config because it's important to not be disturbed by formatting issue in code review as a team.
* We have chosen poetry as package management to reduce any issues of python deps mismatch / resolving for team members.
* We choose english as main language so it's easier for new team members to onboard whatever his language is.

## Additional questions

### Traitement ad-hoc

> Extraire depuis le json produit par la data pipeline le nom du journal qui mentionne le plus de
médicaments différents ?

We have created a small script to answer this question, running:

```bash
python ad_hoc.py
```

will returns

```
('Psychopharmacology', {'ETHANOL', 'TETRACYCLINE'})
```

### Pour aller plus loin

> Quels sont les éléments à considérer pour faire évoluer votre code afin qu’il puisse gérer de grosses
volumétries de données (fichiers de plusieurs To ou millions de fichiers par exemple) ? Pourriez-vous décrire les modifications qu’il faudrait apporter, s’il y en a, pour prendre en considération de
telles volumétries ?

If the input dataset is much bigger (To or millions of files), this program would have an issue cause we are loading data in-memory. Then i would switch pandas with pyspark because with spark we can manipulate dataframe out of memory. The files could be stored in a distributed file storage system (such as aws s3). The spark engine could handle easily such volumes or millions of files to process. With spark we can also size number of executors and resources assigned to the driver / executors and many other parameters for optimization.
To orchestrate the different tasks we might also introduce a workflow management framework (such as airflow) to have a better management of the data pipelines (retries, failures, scheduling etc ...). For instance if loading & preprocessing a dataset takes time and fails, this would enables to retry only this step and not the all workflow.

### SQL

####  First part

> Je vous propose de commencer par réaliser une requête SQL simple permettant de trouver le chiffre
d’affaires (le montant total des ventes), jour par jour, du 1er janvier 2019 au 31 décembre 2019. Le résultat
sera trié sur la date à laquelle la commande a été passée

```sql
select
    sum(prod_price*prod_qty) as ventes,
    date
from TRANSACTION
where date >= '2019-01-01' AND date <= '2019-12-31'
group by date
order by date asc
```

####  Second part

> Réaliser une requête un peu plus complexe qui permet de déterminer, par client et sur la période allant du
1er janvier 2019 au 31 décembre 2019, les ventes meuble et déco réalisées.

```sql
select
    client_id,
    sum(CASE WHEN prod.product_type = 'MEUBLE' THEN trans.prod_price * trans.prod_qty ELSE 0 END) AS ventes_meuble,
    sum(CASE WHEN prod.product_type = 'DECO' THEN trans.prod_price * trans.prod_qty ELSE 0 END) AS ventes_deco
from TRANSACTION trans
left join PRODUCT_NOMENCLATURE prod
on trans.prop_id=prod.product_id
where date >= '2019-01-01' AND date <= '2019-12-31'
group trans.client_id
```
