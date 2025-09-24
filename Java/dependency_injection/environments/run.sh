mvn compile

# Run by specifying the profile on the command line
# mvn exec:java -Dexec.mainClass=com.tps.App -Dspring.profiles.active=sales
# mvn exec:java -Dexec.mainClass=com.tps.App -Dspring.profiles.active=income

# Using profile in application.properties
mvn exec:java -Dexec.mainClass=com.tps.App