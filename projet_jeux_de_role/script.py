import time
start_time = time.time()

txt = "2021-10-21 10:14:21,717 INFO Dev04 SILP-CHUM recepteur etabFA - Journalisation - <enovacomMessage>	<rows>		<variableCdoi>				<archiveIdMessage>155934</archiveIdMessage>				<archiveIdIteration>0</archiveIdIteration>				<route>					<nom>Commun SILP-CHUM route</nom>					<siRecepteurEnTraitement>Dev04 SILP recepteur</siRecepteurEnTraitement>					<communAbntRteScenario/>				</route>			<routage/>			<sortie>				<ack>					<code/>					<base64/>				</ack>				<pretAEnvoyer>					<siRecepteur>Dev04 SILP-CHUM recepteur</siRecepteur>					<date>2021/10/21 10:14:21</date>					<code>Message prêt à envoyer</code>					<code2/>					<commentaire/>				</pretAEnvoyer>			</sortie>		</variableCdoi>	</rows></enovacomMessage>2021-10-22 10:14:21,717 INFO Dev04 SILP-CHUM recepteur etabFA - Journalisation - <enovacomMessage>	<rows>		<variableCdoi>				<archiveIdMessage>155934</archiveIdMessage>				<archiveIdIteration>0</archiveIdIteration>				<route>					<nom>Commun SILP-CHUM route</nom>					<siRecepteurEnTraitement>Dev04 SILP recepteur</siRecepteurEnTraitement>					<communAbntRteScenario/>				</route>			<routage/>			<sortie>				<ack>					<code/>					<base64/>				</ack>				<pretAEnvoyer>					<siRecepteur>Dev04 SILP-CHUM recepteur</siRecepteur>					<date>2021/10/21 10:14:21</date>					<code>Message prêt à envoyer</code>					<code2/>					<commentaire/>				</pretAEnvoyer>			</sortie>		</variableCdoi>	</rows></enovacomMessage>2021-10-23 10:14:21,717 INFO Dev04 SILP-CHUM recepteur etabFA - Journalisation - <enovacomMessage>	<rows>		<variableCdoi>				<archiveIdMessage>155934</archiveIdMessage>				<archiveIdIteration>0</archiveIdIteration>				<route>					<nom>Commun SILP-CHUM route</nom>					<siRecepteurEnTraitement>Dev04 SILP recepteur</siRecepteurEnTraitement>					<communAbntRteScenario/>				</route>			<routage/>			<sortie>				<ack>					<code/>					<base64/>				</ack>				<pretAEnvoyer>					<siRecepteur>Dev04 SILP-CHUM recepteur</siRecepteur>					<date>2021/10/21 10:14:21</date>					<code>Message prêt à envoyer</code>					<code2/>					<commentaire/>				</pretAEnvoyer>			</sortie>		</variableCdoi>	</rows></enovacomMessage>"

x = txt.split("</enovacomMessage>")
y = x[0].split("<enovacomMessage>")
print(y[1])
print("--- %s seconds ---" % (time.time() - start_time))
