from orator.migrations import Migration


class CreateResultsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('results') as table:
            table.increments('id')
            table.timestamps()
            table.integer('train_id').unsigned()
            table.foreign('train_id').references('id').on('trains').on_delete('cascade')
            table.string('key', 100)
            table.string('value', 100)


    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('results')
