from orator.migrations import Migration


class CreateTrainsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('trains') as table:
            table.increments('id')
            table.string('name', 100)
            table.timestamps()

        with self.schema.create('trains_trans') as table:
            table.increments('id')
            table.integer('tran_id').unsigned()
            table.foreign('tran_id').references('id').on('trans').on_delete('cascade')
            table.integer('train_id').unsigned()
            table.foreign('train_id').references('id').on('trains').on_delete('cascade')
            table.string('result', 100)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('trains')
        self.schema.drop('trains_trans')
