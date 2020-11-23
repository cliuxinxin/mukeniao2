from orator.migrations import Migration


class CreateEntriesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('entries') as table:
            table.increments('id')
            table.string('location', 100).unique()
            table.string('label', 100).nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('entries')
